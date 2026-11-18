"""Make caption and chapter tracks from the verified film's displayed-frame clock."""
import argparse
import bisect
import json
import math
from pathlib import Path

PUBLIC_DIR = Path(__file__).resolve().parents[1] / "assets/video/projects/spot-whole-body"
STEM = "warehouse-delivery-continuous"

# Native skill intervals from the independent audit define the chapter boundaries.
CHAPTERS = {
    "reorient": "Right the carton",
    "approach": "Walk around to the pickup side",
    "sit": "Sit beside the carton",
    "load": "Receive the carton and stand",
    "carry": "Carry along the north route",
    "place": "Lower and release into bay B",
    "depart": "Stand and walk away",
}

# Skill subphases stored with each selected native pose anchor descriptions.
DESCRIPTIONS = {
    "reorient": "The warehouse comes into view. Spot starts beside a carton resting on its broad face.",
    "approach_clear": "Spot steps away from the upright carton and walks around to the pickup side.",
    "sit": "Spot lowers onto its rear shins, bringing its back close to the carton.",
    "align": "The arm reaches over the carton and draws it against the rear deck.",
    "load": "Spot stands on four legs with the carton braced between its back and arm.",
    "carry": "Spot carries the carton north of the red fire lane and across the warehouse.",
    "place": "At bay B, Spot lowers the carton onto the floor and releases it upright.",
    "retract": "Spot draws the arm clear of the carton and rises.",
    "depart": "Spot walks clear. The carton stays upright in the receiving bay.",
}


def timestamp(frame, fps):
    millis = round(1000 * frame / fps)
    seconds, millis = divmod(millis, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}.{millis:03}"


def write_track(path, starts, count, fps):
    if starts[0][0] != 0 or any(b[0] <= a[0] for a, b in zip(starts, starts[1:])) or starts[-1][0] >= count:
        raise ValueError("Cues must be in increasing frame order and cover the full film")
    cues = ["WEBVTT", ""]
    for (frame, label), end in zip(starts, [f for f, _ in starts[1:]] + [count], strict=True):
        cues.extend([f"{timestamp(frame, fps)} --> {timestamp(end, fps)}", label, ""])
    path.write_text("\n".join(cues) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("film_clock", type=Path)
    parser.add_argument("continuous_audit", type=Path)
    parser.add_argument("--output", type=Path, default=PUBLIC_DIR)
    args = parser.parse_args()
    clock = json.loads(args.film_clock.read_text())
    audit = json.loads(args.continuous_audit.read_text())
    times, phases, fps = clock["source_time_s"], clock["phase"], clock["fps"]
    if clock["source_trace_sha256"] != audit["source_hashes"]["private/dynamics/trace.npz"]:
        raise ValueError("Clock and audit reference different simulation traces")
    if (len(times) != clock["frames"] or len(times) != len(phases) or not all(map(math.isfinite, times))
            or any(b <= a for a, b in zip(times, times[1:])) or times[0] != 0
            or fps <= 0 or clock["cuts"] != 0 or not audit["outcome"]["completed_order"]):
        raise ValueError("Incomplete or non-monotonic display clock")
    if times[-1] < audit["time_s"][-1] - 0.2:
        raise ValueError("Final state missing from the film")
    chapters = []
    for skill, label in CHAPTERS.items():
        start = audit["stage_metrics"][skill]["interval_s"][0]
        chapters.append((bisect.bisect_right(times, start) if start else 0, label))
    descriptions = [(0 if phase == "reorient" else phases.index(phase), label) for phase, label in DESCRIPTIONS.items()]
    # The audited carton crosses 5 and 80 degrees at native t=4.24 and 6.36 seconds.
    # Map through the source clock because later portions use a different playback speed.
    descriptions.extend([
        (bisect.bisect_left(times, 4.24), "The forefoot and arm tip the carton around a floor edge."),
        (bisect.bisect_left(times, 6.36), "The carton settles on its end as Spot eases off."),
    ])
    args.output.mkdir(parents=True, exist_ok=True)
    write_track(args.output / f"{STEM}.vtt", sorted(descriptions), len(times), fps)
    write_track(args.output / f"{STEM}-chapters.vtt", chapters, len(times), fps)


if __name__ == "__main__":
    main()
