"""
AI Security Curriculum content
Waypoint Compliance Advisory - waypointca.com

Source of truth for the eight curriculum pages. Edit here, then run build.py.

PUBLISHING POSTURE
This is an authored body of knowledge, published as thought leadership and a
reference. It is not an enrollable program and Waypoint does not grant a
degree. "Doctoral-level" is used as a rigor descriptor only. Any language
implying admission, enrollment, or conferral must stay out of this file.

Internal strategy from the source drafts (target institutions, the pitch and
wedge, course-development compensation, open design questions) is deliberately
not represented here and must not be added.

House style: no em dashes. DoD or Department of Defense, never Department of War.
"""

SITE = "https://waypointca.com"
BASE = "/ai-security/curriculum"

AUTHOR = {
    "name": "Cameron Hopkin",
    "creds": "CISSP, CEH, CHFI",
    "email": "cameron@waypointca.com",
}

# ── Pillar ──────────────────────────────────────────────────────────────────

PILLAR = {
    "slug": "",
    "title": "Applied AI Security and Assurance Curriculum",
    "page_title": "Applied AI Security and Assurance Curriculum | Waypoint Compliance Advisory",
    "meta": (
        "A doctoral-level curriculum in applied AI security and assurance, authored by Cameron Hopkin, "
        "CISSP. Seven cores from adversarial ML to AI governance."
    ),
    "lede": (
        "A curriculum for people who will be responsible for AI systems when they fail, not just when "
        "they demo."
    ),
    "sections": [
        ("What this is", [
            "<p>This is a complete doctoral-level curriculum in applied AI security and assurance, "
            "authored by Cameron Hopkin. It is published here as a body of knowledge and a reference, "
            "not as a program you can enroll in. Waypoint Compliance Advisory does not grant degrees. "
            "The structure, sequencing, and credit scope are included because they are the shape of the "
            "argument: they show what a serious treatment of this field actually requires.</p>",

            "<p>It is built with AI security and assurance as the spine rather than a bolt-on. Standard "
            "machine learning content is present but demoted to foundation. The intent is to describe "
            "what it takes to produce someone who can secure, red-team, evaluate, govern, and assure AI "
            "systems at a research level, and defend original applied work in that area.</p>",
        ]),
        ("Who it is written for", [
            "<p>Mid-to-senior practitioners: security engineers, machine learning engineers, governance "
            "and assurance leads, and technical managers who already ship or govern systems and want to "
            "do defensible work on making them trustworthy. It assumes prior programming and a security "
            "or machine learning foundation. Because the orientation is applied, a live problem from "
            "your own work is an asset rather than a distraction.</p>",
        ]),
        ("What a graduate of this curriculum can do", [
            "<p>Someone who works through this material end to end can:</p>",
            "<ol>"
            "<li>Model the threat surface of an AI system end to end and design controls for it.</li>"
            "<li>Build and run adversarial evaluations and red-team programs as security controls, not "
            "afterthoughts.</li>"
            "<li>Engineer AI pipelines with provenance, integrity, and supply-chain guarantees.</li>"
            "<li>Construct and defend an assurance case that a given system is safe and secure enough "
            "for its use.</li>"
            "<li>Situate technical work inside real governance and risk frameworks, including the NIST "
            "AI Risk Management Framework and relevant DoD and federal guidance.</li>"
            "<li>Produce original, publishable applied research others can adopt.</li>"
            "</ol>",
        ]),
    ],
    "gap": [
        "<p>The case for building this is not a hunch. It is what the landscape looks like when you "
        "check it.</p>",

        "<p><strong>AI security exists in higher education, but as a bolt-on rather than a spine.</strong> "
        "Independent analysis of accredited cybersecurity doctorates treats AI and machine learning "
        "security as one of several specialized seminars that vary by program and faculty expertise, "
        "alongside forensics and cryptography <a href=\"#ref-1\">[1]</a>. It is a topic inside a degree, "
        "not the degree.</p>",

        "<p><strong>Where AI security is taught in depth, it stops at the master's level, and even there "
        "it is explicitly shallow on research skills.</strong> Nova Southeastern's M.S. in Artificial "
        "Intelligence Cybersecurity carries NSA validation <a href=\"#ref-2\">[2]</a>, and comparable "
        "concentrations exist elsewhere. But a 2026 review of these programs states plainly that the AI "
        "coursework provides practical literacy, enough to evaluate vendor tools and understand "
        "adversarial risk, without the depth required for model development or red-team AI research "
        "roles <a href=\"#ref-3\">[3]</a>. That missing depth is exactly what doctoral-level work is "
        "for.</p>",

        "<p><strong>The demand signal is real.</strong> Reviews of the field describe rising 2026 demand "
        "from mid-career professionals for exactly these research-adjacent roles: adversarial machine "
        "learning researcher, AI red team analyst, and machine learning security architect "
        "<a href=\"#ref-1\">[1]</a><a href=\"#ref-3\">[3]</a>.</p>",
    ],
    "spine": [
        "<p>Everything before Core 4 exists to make Cores 4 through 7 possible. Someone who works "
        "through this curriculum is not primarily a model builder. They are the person an organization "
        "puts in the room when an AI system has to be trusted with something that matters.</p>",
    ],
    "sequencing": [
        "<p>Cores 1 to 3 form a foundation block taken first, in order. Cores 4 to 7 are the security "
        "spine. Cores 4 and 5 are sequential, because robustness comes before agent red teaming, while "
        "6 and 7 can run in parallel for someone who already has the foundation. The praxis proposal "
        "runs alongside the later cores so it grows out of the work rather than starting cold. The "
        "praxis research follows.</p>",
    ],
}

CREDITS = [
    ("Core 1", "Mathematical and Statistical Foundations for AI", "4", "mathematical-foundations-for-ai"),
    ("Core 2", "Modern Deep Learning and Representation", "4", "modern-deep-learning"),
    ("Core 3", "Language Models, Retrieval, and Agents", "4", "language-models-retrieval-agents"),
    ("Core 4", "Adversarial Machine Learning and Model Robustness", "4", "adversarial-machine-learning"),
    ("Core 5", "LLM and Agent Security: Red Teaming and Evaluation", "4", "llm-agent-security-red-teaming"),
    ("Core 6", "Secure AI Engineering: MLOps, LLMOps, and Supply Chain", "4", "secure-ai-engineering-mlops"),
    ("Core 7", "AI Governance, Assurance, and Risk", "4", "ai-governance-assurance-risk"),
    ("Praxis 1", "Research Methods and Praxis Proposal", "4", None),
    ("Praxis 2", "Praxis Research and Defense", "24", None),
]
CREDIT_TOTAL = "52 credit hours"

PRAXIS = [
    ("Praxis 1: Research Methods and Praxis Proposal",
     "Research methods for an applied engineering doctorate, aimed at turning a live problem into a "
     "defensible research contribution. Covers research methods and design, problem formulation and "
     "literature positioning, framing an original contribution, and proposal development and defense. "
     "The output is a defended praxis proposal, ideally grown from a signature lab in Core 4, 5, 6, or 7."),
    ("Praxis 2: Praxis Research and Defense",
     "Original applied research producing a defensible, adoptable contribution. The expected shape is a "
     "security or assurance method, tool, or evaluation methodology that others in the field can use, "
     "with the rigor to defend it. The output is a completed praxis and successful defense."),
]

# ── Spokes ──────────────────────────────────────────────────────────────────

CORES = [
    {
        "n": 1,
        "slug": "mathematical-foundations-for-ai",
        "code": "Core 1",
        "title": "Mathematical and Statistical Foundations for AI",
        "page_title": "Mathematical and Statistical Foundations for AI | AI Security Curriculum",
        "meta": ("Core 1 of the applied AI security curriculum. Linear algebra, optimization, probability, "
                 "and calibration, framed toward what breaks in real systems."),
        "spine": False,
        "description": (
            "The honest mathematical foundation, modernized and pointed at what breaks in real systems. "
            "Linear algebra, matrix decompositions, optimization, probability, and statistics, each "
            "framed toward downstream security and evaluation concerns rather than taught in isolation."),
        "outcomes": [
            "Implement core numerical methods from scratch.",
            "Reason about conditioning, convergence, and where optimization fails.",
            "Quantify and communicate uncertainty and calibration.",
        ],
        "modules": [
            "Linear algebra and the geometry of high-dimensional space.",
            "Matrix decompositions and why they matter.",
            "Optimization: gradient methods, convexity, and failure modes.",
            "Probability and statistics for machine learning.",
            "Calibration and uncertainty.",
            "Reproducibility and numerical stability.",
        ],
        "lab": ("Implement backpropagation and an optimizer from scratch in "
                "<a href=\"https://pytorch.org/\" rel=\"noopener\">PyTorch</a>, then break it with a "
                "poorly conditioned problem and diagnose why. PyTorch is the deliberate choice: it is "
                "the framework of the research literature this curriculum trains people to read and "
                "extend, used in roughly 85 percent of published deep learning research "
                "<a href=\"" + BASE + "/#ref-4\">[4]</a>."),
        "reading": [],
        "thread": ("Reproducibility and numerical stability as preconditions for any trustworthy "
                   "result."),
    },
    {
        "n": 2,
        "slug": "modern-deep-learning",
        "code": "Core 2",
        "title": "Modern Deep Learning and Representation",
        "page_title": "Modern Deep Learning and Representation | AI Security Curriculum",
        "meta": ("Core 2. Transformers, the PyTorch and Hugging Face stack, LoRA and PEFT fine-tuning, "
                 "diffusion models, and what internal representations leak to an adversary."),
        "spine": False,
        "description": (
            "Replaces the dated bag-of-words and GAN-centric approach with the actual modern stack: "
            "transformers, the Hugging Face and PyTorch ecosystem, and diffusion as the generative "
            "flagship. The models that define the field are built in this ecosystem "
            "<a href=\"" + BASE + "/#ref-5\">[5]</a>."),
        "outcomes": [
            "Explain and implement the transformer end to end.",
            "Fine-tune open models with LoRA and PEFT.",
            "Reason about what representations encode and leak.",
        ],
        "modules": [
            "Transformer architecture, attention, tokenization, and embeddings.",
            "Training dynamics and transfer learning.",
            "Fine-tuning, LoRA, and PEFT.",
            "Diffusion models as the modern generative flagship, with GANs treated as history.",
            "Interpretability primitives and probing.",
            "Representation leakage.",
        ],
        "lab": ("Fine-tune an open model with LoRA using the "
                "<a href=\"https://huggingface.co/\" rel=\"noopener\">Hugging Face</a> ecosystem and "
                "document precisely what changed in its behavior and why."),
        "reading": [],
        "thread": "What a model's internal representations reveal, and what that leaks to an adversary.",
    },
    {
        "n": 3,
        "slug": "language-models-retrieval-agents",
        "code": "Core 3",
        "title": "Language Models, Retrieval, and Agents",
        "page_title": "Language Models, Retrieval, and Agents | AI Security Curriculum",
        "meta": ("Core 3. Building RAG systems and tool-using agents, instrumenting them for retrieval "
                 "and answer quality, and finding their silent failure modes."),
        "spine": False,
        "description": (
            "Foundations through operations for reliable LLM applications, taught so the reliability "
            "question stays live throughout rather than being deferred to the end."),
        "outcomes": [
            "Design and build retrieval-augmented generation systems and tool-using agents.",
            "Instrument them for retrieval quality and answer quality.",
            "Identify their silent failure modes.",
        ],
        "modules": [
            "LLM foundations, prompting, and context engineering.",
            "Retrieval-augmented generation: indexing, chunking, and retrieval quality.",
            "Tool use and function calling.",
            "Agent architectures and memory.",
            "Evaluation and reliability of generated output.",
            "Failure analysis.",
        ],
        "lab": ("Build a retrieval-augmented agent, then instrument it to measure retrieval quality and "
                "answer quality and expose where it quietly breaks."),
        "reading": [],
        "thread": "Where agents fail without signaling it, and how an operator would know.",
    },
    {
        "n": 4,
        "slug": "adversarial-machine-learning",
        "code": "Core 4",
        "title": "Adversarial Machine Learning and Model Robustness",
        "page_title": "Adversarial Machine Learning and Model Robustness | AI Security Curriculum",
        "meta": ("Core 4, first course of the security spine. Evasion, poisoning, backdoors, model "
                 "extraction, membership inference, and the real limits of defenses."),
        "spine": True,
        "description": (
            "A rigorous treatment of the machine learning attack surface and the honest limits of "
            "defenses. This is where the curriculum stops being a machine learning program and becomes "
            "a security one."),
        "outcomes": [
            "Build a full threat model for a machine learning system.",
            "Execute evasion, poisoning, extraction, and inference attacks.",
            "Evaluate robustness and articulate what an evaluation does and does not prove.",
        ],
        "modules": [
            "Threat models for machine learning and the end-to-end attack surface.",
            "Evasion, adversarial examples, and transferability.",
            "Data poisoning and backdoors.",
            "Model extraction and stealing.",
            "Membership inference and privacy attacks.",
            "Defenses and their limits under adaptive attackers.",
        ],
        "lab": ("Poison a training set and then detect the poison. Separately, extract a deployed model "
                "through its API. Deliver both attack and detection as reusable tooling."),
        "reading": [
            "The adversarial examples line of work.",
            "Poisoning and backdoor research.",
            "Membership inference literature.",
            "<a href=\"https://atlas.mitre.org/\" rel=\"noopener\">MITRE ATLAS</a> as the threat "
            "taxonomy, which extends MITRE ATT&amp;CK to adversarial tactics against AI systems "
            "<a href=\"" + BASE + "/#ref-6\">[6]</a>.",
        ],
        "thread": "A defense that survives an adaptive attacker, not just a static benchmark.",
    },
    {
        "n": 5,
        "slug": "llm-agent-security-red-teaming",
        "code": "Core 5",
        "title": "LLM and Agent Security: Red Teaming and Evaluation",
        "page_title": "LLM and Agent Security: Red Teaming and Evaluation | Full Syllabus",
        "meta": ("The complete Core 5 syllabus. Prompt injection, jailbreaks, guardrail evasion, agent "
                 "containment, and evaluation harnesses as security controls."),
        "spine": True,
        "flagship": True,
        "description": (
            "The flagship course, and the one that defines the curriculum. It treats large language "
            "model and agent systems as targets and teaches how to attack, defend, evaluate, and govern "
            "them at a research level. The full syllabus is published below."),
        "outcomes": [
            "Execute direct and indirect prompt-injection and jailbreak attacks against LLM and agent systems.",
            "Design containment and least-privilege controls for autonomous tools.",
            "Build evaluation harnesses that function as security controls.",
            "Run a structured red-team engagement and report defensible findings.",
        ],
        "modules": [
            "The LLM and agent threat surface.",
            "Prompt injection, direct and indirect, and data exfiltration through agents.",
            "Jailbreaks and guardrail evasion.",
            "Tool and agent containment and least privilege for autonomous systems.",
            "Evaluation as a safety and security control.",
            "Building evaluation harnesses.",
            "Running a red-team program and reporting.",
            "Capstone engagement.",
        ],
        "lab": ("Stand up an evaluation and red-team harness against a tool-using agent, run a "
                "structured engagement, and deliver a findings report plus the reusable harness."),
        "reading": [
            "<a href=\"https://owasp.org/www-project-top-10-for-large-language-model-applications/\" "
            "rel=\"noopener\">OWASP Top 10 for LLM Applications 2025 (v2.0)</a>, published 18 November "
            "2024 by the <a href=\"https://genai.owasp.org/\" rel=\"noopener\">OWASP GenAI Security "
            "Project</a>, as the risk catalogue <a href=\"" + BASE + "/#ref-7\">[7]</a>"
            "<a href=\"" + BASE + "/#ref-8\">[8]</a>.",
            "The OWASP Top 10 for Agentic Applications 2026 for autonomous tool-using systems "
            "<a href=\"" + BASE + "/#ref-9\">[9]</a>.",
            "<a href=\"https://atlas.mitre.org/\" rel=\"noopener\">MITRE ATLAS</a> for red-team "
            "scenario design <a href=\"" + BASE + "/#ref-6\">[6]</a>.",
            "Current model-evaluation and red-teaming methodology work.",
        ],
        "thread": ("A reusable evaluation or red-team methodology others can adopt, which is a natural "
                   "praxis seed."),
    },
    {
        "n": 6,
        "slug": "secure-ai-engineering-mlops",
        "code": "Core 6",
        "title": "Secure AI Engineering: MLOps, LLMOps, and Supply Chain",
        "page_title": "Secure AI Engineering: MLOps, LLMOps, and Supply Chain | AI Security Curriculum",
        "meta": ("Core 6. Data and model pipeline integrity, model provenance and signing, SBOM for "
                 "models, monitoring and incident response for AI systems in production."),
        "spine": True,
        "description": (
            "Real production security for AI systems. This is also where the curriculum is honest about "
            "tooling: PyTorch is the research and training standard, but TensorFlow's production "
            "ecosystem still leads a large share of enterprise deployment "
            "<a href=\"" + BASE + "/#ref-4\">[4]</a>, so the material covers securing the stack that "
            "production actually runs, not only the one research prefers."),
        "outcomes": [
            "Build data and model pipelines with integrity guarantees.",
            "Establish model and dependency provenance.",
            "Design monitoring and incident response for AI systems in production.",
            "Secure both research-native and production-native toolchains.",
        ],
        "modules": [
            "Data pipelines and their integrity guarantees.",
            "Model and dependency supply chain: provenance, signing, and SBOM for models.",
            "Deployment and serving across research and production stacks.",
            "Monitoring, drift, and incident response for AI systems.",
            "Secrets, access, and isolation in AI infrastructure.",
            "Tamper detection end to end.",
        ],
        "lab": ("Build a pipeline with provenance and tamper detection across the whole path from data "
                "to deployed model."),
        "reading": [],
        "thread": "Practical integrity guarantees for a model supply chain.",
    },
    {
        "n": 7,
        "slug": "ai-governance-assurance-risk",
        "code": "Core 7",
        "title": "AI Governance, Assurance, and Risk",
        "page_title": "AI Governance, Assurance, and Risk | AI Security Curriculum",
        "meta": ("Core 7. NIST AI RMF and its GenAI Profile, ISO/IEC 42001, the EU AI Act, assurance cases, "
                 "and measurable assurance versus paper compliance."),
        "spine": True,
        "description": (
            "Ties the technical spine to policy, compliance, and assurance. This is where alignment and "
            "post-training are treated as governance problems, and where measurable assurance is "
            "separated from paper compliance."),
        "outcomes": [
            "Apply recognized AI risk frameworks.",
            "Construct and stress-test an assurance case.",
            "Evaluate post-training and alignment methods as governance controls.",
            "Argue accountability without hand-waving.",
        ],
        "modules": [
            "Risk frameworks: the NIST AI Risk Management Framework and its Generative AI Profile "
            "(AI 600-1), plus relevant DoD and federal guidance.",
            "Standards and law: ISO/IEC 42001 as the first certifiable AI management system standard, "
            "and the EU AI Act.",
            "Assurance cases and how you argue a system is safe enough.",
            "Post-training as governance: RLHF, DPO, reward modeling, and their failure modes.",
            "Ethics, societal impact, and accountability.",
            "Measurable assurance versus paper compliance.",
        ],
        "lab": "Write an assurance case for a real deployed system and then stress-test it to failure.",
        "reading": [
            "<a href=\"https://www.nist.gov/itl/ai-risk-management-framework\" rel=\"noopener\">NIST AI "
            "Risk Management Framework</a> and its Generative AI Profile (AI 600-1) "
            "<a href=\"" + BASE + "/#ref-6\">[6]</a>.",
            "<a href=\"https://www.iso.org/standard/81230.html\" rel=\"noopener\">ISO/IEC 42001</a>, "
            "the first certifiable AI management system standard "
            "<a href=\"" + BASE + "/#ref-9\">[9]</a>.",
            "The <a href=\"https://artificialintelligenceact.eu/\" rel=\"noopener\">EU AI Act</a>, "
            "including its penalty regime <a href=\"" + BASE + "/#ref-9\">[9]</a>.",
        ],
        "thread": ("What separates measurable assurance from compliance theater, and how to close that "
                   "gap."),
    },
]

# ── Core 5 full syllabus ────────────────────────────────────────────────────

SYLLABUS = {
    "meta_line": "4 credits | Doctoral level | 14 weeks, compressible to 7 at two modules per week",
    "description": [
        "<p>This course treats large language model and agent systems as targets and teaches students "
        "to attack, defend, evaluate, and govern them at a research level. It covers direct and "
        "indirect prompt injection, jailbreaks, guardrail and defense evasion, and data exfiltration "
        "through tool-using agents. Students design containment and least-privilege controls for "
        "autonomous systems, and build evaluation harnesses that function as security controls rather "
        "than as accuracy metrics.</p>",
        "<p>The course is built around recognized industry frameworks and culminates in a structured "
        "red-team engagement against a provided agent, delivered as a defensible findings report plus a "
        "reusable methodology.</p>",
        "<p>It is deliberately dual-purpose. Viewed as academic work, it is outcome-mapped, "
        "literature-anchored, and assessed through produced research artifacts rather than quizzes. "
        "Viewed as practitioner training, every module ends in something runnable against a real "
        "system, and the signature deliverables, a harness and a methodology, are kept and reused after "
        "the course ends.</p>",
    ],
    "prerequisites": [
        "Core 3 (Language Models, Retrieval, and Agents), or demonstrated equivalent: the ability to "
        "build a basic retrieval-augmented or tool-using agent.",
        "Working Python, comfort at the command line, and familiarity with HTTP APIs.",
        "Recommended: Core 4 (Adversarial Machine Learning) taken concurrently or prior.",
    ],
    "outcomes": [
        "Construct a complete threat model for an LLM or agent system, mapped to OWASP and MITRE ATLAS "
        "categories.",
        "Execute direct and indirect prompt-injection, jailbreak, and guardrail-evasion attacks against "
        "LLM and agent systems within an authorized scope.",
        "Demonstrate data exfiltration and unauthorized action through a tool-using agent, and design "
        "containment and least-privilege controls that prevent it.",
        "Design and build an evaluation harness that operates as a security control, including "
        "automated adversarial evaluation.",
        "Plan and run a structured red-team engagement with defined rules of engagement, and produce a "
        "findings report that meets professional and responsible-disclosure standards.",
        "Produce a reusable evaluation or red-team methodology that others can adopt, positioned as an "
        "original contribution suitable to seed praxis research.",
    ],
    "environment": [
        "<p>All labs run in an isolated, provided sandbox against provided targets. Students never "
        "attack third-party or production systems. See the ethics and legal policy below.</p>",
        "<p>Per standard, all work is done inside a Python virtual environment:</p>",
    ],
    "venv": """# Create a project virtual environment
python3 -m venv .venv

# Activate it
source .venv/bin/activate        # macOS / Linux
# .venv\\Scripts\\activate         # Windows PowerShell

# Upgrade pip, then install the course baseline
python -m pip install --upgrade pip
pip install -r requirements.txt""",
    "environment_after": [
        "<p>A starter <code>requirements.txt</code> provides the PyTorch and Hugging Face stack, an "
        "HTTP client, an evaluation framework, and the harness scaffolding. Students deactivate with "
        "<code>deactivate</code> when done and never install course packages system-wide.</p>",
        "<p>PyTorch is the standard here because it is the framework of the research literature this "
        "course trains students to read and extend.</p>",
    ],
    "anchors_intro": (
        "<p>These are the fixed, citable anchors every student reads. Specific research-paper "
        "assignments attach per module and are finalized each offering to stay current.</p>"),
    "anchors": [
        "<a href=\"https://owasp.org/www-project-top-10-for-large-language-model-applications/\" "
        "rel=\"noopener\">OWASP Top 10 for LLM Applications 2025 (v2.0)</a>, OWASP GenAI Security Project.",
        "OWASP Top 10 for Agentic Applications 2026, "
        "<a href=\"https://genai.owasp.org/\" rel=\"noopener\">OWASP GenAI Security Project</a>, for the "
        "agent modules.",
        "<a href=\"https://atlas.mitre.org/\" rel=\"noopener\">MITRE ATLAS</a>, the adversarial threat "
        "landscape for AI systems, which extends MITRE ATT&amp;CK.",
        "<a href=\"https://www.nist.gov/itl/ai-risk-management-framework\" rel=\"noopener\">NIST AI Risk "
        "Management Framework</a> and its Generative AI Profile (AI 600-1).",
    ],
    "anchors_after": (
        "<p>Supplementary governance framing: "
        "<a href=\"https://www.iso.org/standard/81230.html\" rel=\"noopener\">ISO/IEC 42001</a> and the "
        "<a href=\"https://artificialintelligenceact.eu/\" rel=\"noopener\">EU AI Act</a>, both treated "
        "in depth in <a href=\"" + BASE + "/ai-governance-assurance-risk/\">Core 7</a> and referenced "
        "here for context. Per-module research readings cover foundational indirect prompt injection "
        "research, jailbreak and guardrail-evasion literature, agent containment and least-privilege "
        "work, automated red-teaming and adversarial evaluation methodology, and current model system "
        "cards and safety evaluations from frontier labs as living case studies.</p>"),
    "schedule": [
        ("Unit 1: Foundations and threat modeling", [
            ("Week 1", "Framing, ethics, and the attack surface.",
             "Why LLM and agent security is distinct from classic application security. Ethics and legal "
             "policy, rules of engagement, responsible disclosure. Environment setup.",
             "Lab 0: stand up the sandbox and confirm access."),
            ("Week 2", "Threat modeling LLM and agent systems.",
             "Walk the OWASP Top 10 for LLM Applications end to end and map it to MITRE ATLAS.",
             "Lab 1: produce a first threat model of the provided target."),
        ]),
        ("Unit 2: Attacking the model", [
            ("Week 3", "Direct prompt injection and jailbreaks.",
             "Instruction override, system-prompt extraction, and jailbreak patterns.",
             "Lab 2: direct injection and jailbreak against the sandbox model."),
            ("Week 4", "Indirect prompt injection and exfiltration.",
             "Attacks delivered through retrieved or tool-fetched content, and data exfiltration paths "
             "through agents.",
             "Lab 3: plant an indirect payload the agent ingests."),
            ("Week 5", "Guardrail and defense evasion.",
             "How guardrails work and how they fail, and evaluating a defense honestly.",
             "Lab 4: bypass a provided guardrail and document why it failed."),
        ]),
        ("Unit 3: Attacking the agent", [
            ("Week 6", "The agentic threat surface.",
             "OWASP Top 10 for Agentic Applications 2026: excessive agency, tool abuse, and multi-step "
             "attacks.",
             "Lab 5: chain a multi-step agent attack."),
            ("Week 7", "Containment and least privilege.",
             "Sandboxing tools, scoping permissions, human-in-the-loop controls, and where they hold.",
             "Lab 6: design and implement a containment control that stops your Week 6 attack."),
        ]),
        ("Unit 4: Evaluation as a security control", [
            ("Week 8", "Midterm checkpoint and evaluation foundations.",
             "Threat model deliverable due. Evaluation as a control rather than a metric: what to "
             "measure and why.", None),
            ("Week 9", "Building evaluation harnesses I.",
             "Designing security evaluations, test-case design, and measuring attack success and "
             "defense coverage.",
             "Lab 7: build the harness core."),
            ("Week 10", "Building evaluation harnesses II.",
             "Automated and adversarial evaluation, and scaling red-team pressure.",
             "Lab 8: add automated adversarial evaluation to the harness."),
        ]),
        ("Unit 5: Engagement and contribution", [
            ("Week 11", "Running a red-team engagement.",
             "Scoping, rules of engagement, methodology, and evidence handling. Capstone scope assigned.",
             None),
            ("Week 12", "Reporting and responsible disclosure.",
             "Findings structure, severity, reproducibility, and disclosure ethics.", None),
            ("Week 13", "Capstone engagement.",
             "Lab-intensive. Students run their structured engagement against the capstone target using "
             "their own harness.", None),
            ("Week 14", "Defense and methodology.",
             "Capstone findings presentations and defense. Final findings report and reusable "
             "methodology due.", None),
        ]),
    ],
    "assessment_intro": (
        "<p>Assessment is entirely through produced artifacts. There are no quizzes or exams.</p>"),
    "assessment": [
        ("Threat model deliverable (Week 8)", "20%", "Outcome 1: rigorous, framework-mapped threat modeling"),
        ("Lab portfolio and evaluation harness", "25%", "Outcomes 2 to 4: hands-on attack, containment, and a working harness"),
        ("Red-team capstone engagement and findings report", "35%", "Outcome 5: end-to-end engagement at professional standard"),
        ("Reusable evaluation or red-team methodology", "15%", "Outcome 6: an original, adoptable contribution"),
        ("Literature discussion leadership and participation", "5%", "Engagement with primary sources"),
    ],
    "assessment_after": (
        "<p><strong>Passing at the doctoral level requires demonstrated original thinking in the "
        "methodology component, not merely successful attacks.</strong> A student who breaks every "
        "target but cannot generalize a reusable method has not yet met the bar.</p>"),
    "rubric_intro": "<p>The capstone is scored on five criteria, each 1 to 5:</p>",
    "rubric": [
        ("Threat model rigor", "Complete, framework-mapped, and honest about scope and assumptions."),
        ("Technical execution", "Attacks and controls are real, reproducible, and correctly understood."),
        ("Evaluation methodology", "The harness measures the right things and the student can defend why."),
        ("Findings quality and disclosure", "The report is clear, severity is justified, and disclosure ethics are sound."),
        ("Reproducibility and reuse", "Another practitioner could pick up the harness and method and apply them."),
    ],
    "ethics_intro": "<p>This is offensive-security material, and the boundaries are not optional.</p>",
    "ethics": [
        "All offensive work is performed only against provided targets in the provided sandbox, within "
        "the assigned scope and rules of engagement.",
        "Students never test, attack, or probe any third-party, employer, or production system without "
        "separate, explicit, written authorization from that system's owner. Coursework is not "
        "authorization.",
        "All findings are handled under responsible-disclosure principles. Nothing from this course is "
        "used to harm a live system or a real user.",
        "These techniques are dual-use. Students are expected to hold the professional and ethical "
        "standard their certifications demand. Violations carry consequences beyond any academic "
        "setting.",
    ],
}

# ── References ──────────────────────────────────────────────────────────────
# Renumbered from the source draft after the internal-strategy sections were
# removed, so numbering is contiguous and every entry is still cited in the
# published text. All URLs verified reachable at build time except iso.org,
# which blocks automated requests but is the authoritative source.

REFERENCES = [
    ("Cybersecurity Guide. \"PhD in Cybersecurity: Programs, Requirements, and Career Outcomes.\"",
     "https://cybersecurityguide.org/programs/phd-in-cybersecurity/"),
    ("Nova Southeastern University, College of Computing, AI, and Cybersecurity. \"Doctoral Degrees.\"",
     "https://computing.nova.edu/degrees/doctoral/index.html"),
    ("Cybersecurity Guide. \"AI Cybersecurity Master's Degree Programs: 2026 Guide and Comparison.\"",
     "https://cybersecurityguide.org/programs/ai-cybersecurity-masters-degree/"),
    ("Second Talent. \"PyTorch vs TensorFlow: Usage, Popularity and Performance in 2026.\"",
     "https://www.secondtalent.com/resources/pytorch-vs-tensorflow-usage-popularity-and-performance/"),
    ("LazyProgrammer. \"PyTorch vs. TensorFlow: Full Overview 2025 Guide.\"",
     "https://lazyprogrammer.me/pytorch-vs-tensorflow/"),
    ("Palo Alto Networks. \"Securing AI's Front Lines\" (MITRE ATLAS, NIST AI RMF Govern, Map, Measure, Manage).",
     "https://www.paloaltonetworks.com/resources/whitepapers/securing-ai-s-front-lines"),
    ("OWASP GenAI Security Project. \"OWASP Top 10 for LLM Applications 2025.\"",
     "https://owasp.org/www-project-top-10-for-large-language-model-applications/"),
    ("Articsledge. \"OWASP Top 10 for LLM Applications (Complete Guide)\" (publication date, v2.0).",
     "https://www.articsledge.com/post/owasp-top-10-for-llm-applications"),
    ("Vectra AI. \"What Is GenAI Security? Risks, Threats and Best Practices\" (OWASP Agentic 2026, "
     "ISO/IEC 42001, EU AI Act).",
     "https://www.vectra.ai/topics/genai-security"),
]

REFERENCES_NOTE = (
    "Sources current as of August 2026. Framework references (OWASP, MITRE ATLAS, NIST AI RMF, "
    "ISO/IEC 42001, EU AI Act) should be read against their latest published editions.")
