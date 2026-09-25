// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-about-me",
    title: "About Me",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-publications",
          title: "Publications",
          description: "A list of my academic publications and conference presentations.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/publications/";
          },
        },{id: "nav-projects",
          title: "Projects",
          description: "Research in tactile sensing, robot manipulation, extended reality, and multi-agent systems.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/projects/";
          },
        },{id: "nav-repositories",
          title: "Repositories",
          description: "Public code and project repositories related to my research.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/repositories/";
          },
        },{id: "nav-curriculum-vitae",
          title: "Curriculum Vitae",
          description: "Selected experience and publications, updated September 2026.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/cv/";
          },
        },{id: "news-started-b-s-in-computer-engineering-at-the-university-of-minnesota-twin-cities",
          title: 'Started B.S. in Computer Engineering at the University of Minnesota, Twin Cities.',
          description: "",
          section: "News",},{id: "news-started-m-s-in-robotics-at-the-university-of-minnesota-twin-cities",
          title: 'Started M.S. in Robotics at the University of Minnesota, Twin Cities.',
          description: "",
          section: "News",},{id: "news-completed-the-university-of-minnesota-m-s-in-robotics-program-minnesota-robotics-institute-graduation-update",
          title: 'Completed the University of Minnesota M.S. in Robotics program. Minnesota Robotics Institute graduation...',
          description: "",
          section: "News",},{id: "news-published-co-author-talk-through-it-ra-l-2024",
          title: 'Published: Co-Author Talk Through It (RA-L 2024)',
          description: "",
          section: "News",handler: () => {
              window.location.href = "/news/TalkThroughIt/";
            },},{id: "news-started-ph-d-in-computer-science-robotics-focus-at-the-university-of-minnesota-twin-cities",
          title: 'Started Ph.D. in Computer Science (Robotics focus) at the University of Minnesota, Twin...',
          description: "",
          section: "News",},{id: "news-posted-the-spark-remote-a-cost-effective-system-for-remote-bimanual-robot-teleoperation-preprint-as-lead-author-with-co-author-karthik-desingh-it-presents-a-low-cost-setup-for-remote-bimanual-manipulation-research",
          title: 'Posted the SPARK-Remote: A Cost-Effective System for Remote Bimanual Robot Teleoperation preprint as...',
          description: "",
          section: "News",},{id: "news-presented-spark-remote-at-the-icra-2025-workshop-on-human-centric-multilateral-teleoperation-workshop-contributions",
          title: 'Presented SPARK-Remote at the ICRA 2025 Workshop on Human-Centric Multilateral Teleoperation. Workshop contributions....',
          description: "",
          section: "News",},{id: "news-shared-spark-remote-at-the-2025-midwest-robotics-workshop",
          title: 'Shared SPARK-Remote at the 2025 Midwest Robotics Workshop.',
          description: "",
          section: "News",},{id: "news-auginsert-accepted-at-iros-2025",
          title: 'AugInsert accepted at IROS 2025',
          description: "",
          section: "News",handler: () => {
              window.location.href = "/news/2025-08-01-auginsert-accepted/";
            },},{id: "news-three-papers-i-co-authored-on-remote-thrombectomy-and-cerebrovascular-navigation-were-accepted-to-the-2026-design-of-medical-devices-conference",
          title: 'Three papers I co-authored on remote thrombectomy and cerebrovascular navigation were accepted to...',
          description: "",
          section: "News",},{id: "news-the-university-of-minnesota-featured-my-robotics-and-tactile-sensing-research",
          title: 'The University of Minnesota featured my robotics and tactile-sensing research.',
          description: "",
          section: "News",},{id: "news-our-three-design-of-medical-devices-2026-papers-are-published-by-asme-covering-a-telerobotic-guidewire-platform-vascular-route-planning-and-the-strokenav2d-dataset",
          title: 'Our three Design of Medical Devices 2026 papers are published by ASME, covering...',
          description: "",
          section: "News",},{id: "news-joined-northrop-grumman-space-systems-ai-foundations-team-as-a-graduate-research-fellow-studying-supervised-emergence-in-multi-agent-ai-systems-experience-and-cv",
          title: 'Joined Northrop Grumman Space Systems’ AI Foundations team as a graduate research fellow,...',
          description: "",
          section: "News",},{id: "news-our-paper-tailorable-force-sensing-skins-for-manipulators-using-textile-and-additive-manufacturing-was-accepted-to-iros-2026-this-work-is-with-heidi-woelfle-brad-holschuh-and-karthik-desingh-project-page",
          title: 'Our paper Tailorable Force-Sensing Skins for Manipulators Using Textile and Additive Manufacturing was...',
          description: "",
          section: "News",},{id: "news-recorded-an-exploratory-zero-shot-blue-marker-pickup-on-the-thunder-ur5e-using-wrist-camera-observations-and-a-language-model-controller-this-is-one-demonstration-with-video",
          title: 'Recorded an exploratory zero-shot blue-marker pickup on the Thunder UR5e using wrist-camera observations...',
          description: "",
          section: "News",},{id: "news-our-tailorable-force-sensing-skins-work-was-accepted-as-a-poster-at-the-iros-2026-scalable-tactile-sensing-for-dexterous-manipulation-workshop",
          title: 'Our tailorable force-sensing skins work was accepted as a poster at the IROS...',
          description: "",
          section: "News",},{id: "news-magpie-a-magnetic-piezoresistive-tactile-skin-was-accepted-for-an-oral-presentation-at-the-iros-2026-scalable-tactile-sensing-for-dexterous-manipulation-workshop-i-developed-this-work-with-breck-school-students-jackson-goodrich-and-eytan-krebs-and-with-karthik-desingh-project-overview",
          title: 'MagPie: A Magnetic-Piezoresistive Tactile Skin was accepted for an oral presentation at the...',
          description: "",
          section: "News",},{id: "news-the-quest-3-sentmap-world-mapper-recorded-data-demo-reconstructed-three-objects-from-headset-observations-live-walkthrough-validation-remains-open",
          title: 'The Quest 3 SentMap / World Mapper recorded-data demo reconstructed three objects from...',
          description: "",
          section: "News",},{id: "news-packaged-the-lite6-a2-full-surface-tactile-skin-design-including-revision-f-wireless-matrix-electronics-interfaces-and-audited-printable-geometry-physical-fit-and-sensing-tests-remain-open",
          title: 'Packaged the Lite6 A2 full-surface tactile-skin design, including Revision F wireless matrix electronics...',
          description: "",
          section: "News",},{id: "projects-alem-multi-agent-coordination",
          title: 'Alem Multi-Agent Coordination',
          description: "Experiments on communication, specialization, and leadership in a shared multi-agent world.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/Alem/";
            },},{id: "projects-auginsert",
          title: 'AugInsert',
          description: "Data augmentation for robust visual-force policies in contact-rich assembly (IROS 2025).",
          section: "Projects",handler: () => {
              window.location.href = "/projects/AugInsert/";
            },},{id: "projects-contact-aware-manipulation",
          title: 'Contact-Aware Manipulation',
          description: "Exploring inverse kinematics and whole-body strategies that respond to contact along a robot&#39;s body.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/Contact_Manipulation/";
            },},{id: "projects-g1-locomotion-and-whole-body-learning",
          title: 'G1 Locomotion and Whole-Body Learning',
          description: "Simulation studies of humanoid walking, supported pickup, and large-object enclosure.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/G1_Learning/";
            },},{id: "projects-visual-futures-for-manipulation",
          title: 'Visual Futures for Manipulation',
          description: "Exploring whether generated future video can guide robot actions, and where visual plans fall short.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/Gen_AI/";
            },},{id: "projects-magpie-tactile-skin",
          title: 'MagPie Tactile Skin',
          description: "A modular magnetic and piezoresistive skin, developed with Breck School students and accepted for an IROS 2026 workshop oral presentation.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/MagPie/";
            },},{id: "projects-quest-3-sentmap-world-mapper",
          title: 'Quest 3 SentMap / World Mapper',
          description: "A mixed-reality room mapper with measured geometry and progressive object reconstruction from Quest observations.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/Quest_SentMap/";
            },},{id: "projects-robot-wide-tactile-skin-design",
          title: 'Robot-Wide Tactile Skin Design',
          description: "Procedural CAD for layered sensing shells over UR5e, Spot, and G1 link geometry.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/Robot_Skins/";
            },},{id: "projects-spark-remote",
          title: 'SPARK-Remote',
          description: "An accessible remote bimanual teleoperation system for the RPM Lab&#39;s dual-arm platform (ICRA 2025 workshop).",
          section: "Projects",handler: () => {
              window.location.href = "/projects/Spark_Remote/";
            },},{id: "projects-spotnlp",
          title: 'SpotNLP',
          description: "A natural-language and gesture interface for Boston Dynamics Spot, with human following and semantic navigation demos.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/SpotNLP/";
            },},{id: "projects-remote-stroke-intervention-robotics",
          title: 'Remote Stroke Intervention Robotics',
          description: "Telerobotic guidewires, vascular path planning, and learning data from a University of Minnesota–Medtronic collaboration.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/Stroke_Robotics/";
            },},{id: "projects-tactile-materials-and-conformal-interfaces",
          title: 'Tactile Materials and Conformal Interfaces',
          description: "Experimental sensor coupons and connected laminate patterns for surfaces that must bend around a robot.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/Tactile_Materials/";
            },},{id: "projects-tailorable-force-sensing-skins",
          title: 'Tailorable Force-Sensing Skins',
          description: "Textile and additive-manufactured sensing layers for whole-arm contact; accepted at IROS 2026.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/Tactile_Skin/";
            },},{id: "projects-talk-through-it",
          title: 'Talk Through It',
          description: "End-user-directed robot manipulation learning through interactive feedback (RA-L 2024).",
          section: "Projects",handler: () => {
              window.location.href = "/projects/Talk_Through_It/";
            },},{id: "projects-astra-gpt-6-zero-shot-ur5-manipulation",
          title: 'Astra / GPT-6 Zero-Shot UR5 Manipulation',
          description: "An exploratory blue-marker pickup on the physical Thunder UR5e using wrist-camera observations.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/UR5_Zero_Shot/";
            },},{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%69%6D%64%69%65%30%32%32@%75%6D%6E.%65%64%75", "_blank");
        },
      },{
        id: 'social-linkedin',
        title: 'LinkedIn',
        section: 'Socials',
        handler: () => {
          window.open("https://www.linkedin.com/in/adam-imdieke-453225257", "_blank");
        },
      },{
        id: 'social-scholar',
        title: 'Google Scholar',
        section: 'Socials',
        handler: () => {
          window.open("https://scholar.google.com/citations?user=HLB6l_EAAAAJ", "_blank");
        },
      },{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
