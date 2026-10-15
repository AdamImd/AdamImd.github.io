"""Package hash-bound native HD Isaac Lab renders for the Spot project page.

Original simulator traces and rendering tools remain in the private research
repository. This presentation step verifies and copies approved native pixels.
"""
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import shutil
import subprocess


def digest(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-dir', required=True, type=Path)
    parser.add_argument('--output-root', required=True, type=Path)
    parser.add_argument('--recipe', type=Path, default=Path(__file__).with_name('spotrl-media-sources.json'))
    args = parser.parse_args()
    recipe = json.loads(args.recipe.read_text())
    metadata_path = args.source_dir/'metadata.json'
    assert digest(metadata_path) == recipe['native_metadata_sha256']
    native = json.loads(metadata_path.read_text())
    assert native['status'] == 'complete'
    video_dir = args.output_root/'assets/video/projects/spot-whole-body'
    image_dir = args.output_root/'assets/img/projects/spot-whole-body'
    video_dir.mkdir(parents=True, exist_ok=True); image_dir.mkdir(parents=True, exist_ok=True)
    clips = []
    for selection in recipe['clips']:
        clip = next(row for row in native['clips'] if row['id'] == selection['id'])
        assert (clip['width'],clip['height'],clip['fps']) == (1920,1080,25)
        assert clip['native_camera_pixels'] and clip['frames'] > 100
        source = args.source_dir/clip['file']
        assert digest(source) == clip['video_sha256'] == selection['video_sha256']
        info = json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(source)]))
        stream = next(row for row in info['streams'] if row['codec_type'] == 'video')
        assert (stream['width'],stream['height'],stream['codec_name']) == (1920,1080,'h264')
        assert Fraction(stream['avg_frame_rate']) == 25
        assert abs(float(info['format']['duration'])-clip['seconds']) < .05
        poster_source = args.source_dir/selection['poster_source']
        assert digest(poster_source) == selection['poster_sha256']
        poster = image_dir/(clip['id']+'.jpg')
        shutil.copyfile(source, video_dir/clip['file']); shutil.copyfile(poster_source,poster)
        clips.append({**clip,'poster':poster.name,'poster_sha256':digest(poster),'output_duration':clip['seconds'],'selection':selection['selection']})
    card = image_dir/'spot-card.jpg'; shutil.copyfile(image_dir/'box-tipping.jpg',card)
    manifest = {'schema_version':2,'scope':recipe['scope'],'sources':recipe['sources'],
                'native_render':{'source_commit':recipe['renderer_source_commit'],'metadata_sha256':recipe['native_metadata_sha256'],
                                 'render_settings':native['render_settings'],'motion':native['motion'],'native_camera_pixels':True},
                'clips':clips,'card':{'file':card.name,'from':'box-tipping','sha256':digest(card)}}
    (video_dir/'provenance.json').write_text(json.dumps(manifest,indent=2)+'\n')
    for path in [*video_dir.iterdir(),*image_dir.iterdir()]: path.chmod(0o644)
    print(json.dumps({'status':'complete','clips':len(clips),'native_resolution':'1920x1080','fps':25}))


if __name__ == '__main__': main()
