"""Capability statement content — one entry per market.

Edit this file to change what appears in the PDFs, then run `python3 build.py`.
Shared blocks (contact, credentials, metrics, NAICS, company data) live in COMMON
so a credential update only has to happen once.
"""

COMMON = {
    "company": "WAYPOINT COMPLIANCE ADVISORY, LLC",
    "cert_band": "SBA CERTIFIED SDVOSB  |  UEI: K2NVWB4QXKN6  |  CAGE: 14Z63",
    "contact": [
        ("Cameron Hopkin, CISSP", "name"),
        ("Principal Consultant", "role"),
        ("cameron@waypointca.com", "plain"),
        ("waypointca.com", "plain"),
    ],
    "credentials": [
        ("CISSP", "ISC2"),
        ("CEH", "EC-Council"),
        ("CHFI", "EC-Council"),
        ("MS Cybersecurity & Info Assurance", ""),
        ("BS Software Engineering", ""),
        ("MBA", "2026"),
    ],
    "metrics": [
        ("21+", "years cybersecurity experience"),
        ("10", "years U.S. Navy service"),
        ("$22M+", "defense budgets managed"),
        ("700+", "accounts analyzed (11 investigations)"),
        ("52+", "critical vulnerabilities remediated"),
        ("60%", "AWS cost reduction (HHS OIG)"),
        ("28", "engineers led through CNSSI audit"),
    ],
    "naics": [
        ("541512", "Computer Systems Design"),
        ("541519", "Other Computer Services"),
        ("541611", "Management Consulting"),
        ("541690", "Other Technical Consulting"),
        ("611420", "Computer Training"),
    ],
    "company_data": [
        "SBA Certified SDVOSB (App #63605)",
        "UEI: K2NVWB4QXKN6",
        "CAGE Code: 14Z63",
        "90% VA Disability Rating",
    ],
    "footer_left": "waypointca.com  |  cameron@waypointca.com  |  DeLand, Florida",
    "footer_right": "SBA Certified SDVOSB  |  CAGE: 14Z63",
}

# Past performance is shared across all four statements but each market leads with
# the engagement most relevant to it, so ordering is set per-market via `pp_order`.
PAST_PERFORMANCE = {
    "hhs": (
        "HHS Office of Inspector General",
        "Lead Security Engineer embedded across 13 production teams. NIST RMF, FISMA "
        "ATO maintenance, HIPAA Security Rule implementation for federal healthcare systems.",
        "60% AWS cost reduction while strengthening security posture. Zero compliance findings across audit cycles.",
    ),
    "uscis": (
        "U.S. Department of Homeland Security / USCIS",
        "Security architecture and access control for federal identity management systems. "
        "NIST 800-53 Rev 5 control mapping, FedRAMP boundary scoping, and ATO documentation.",
        "Delivered ATO-ready documentation for cloud-hosted IAM components supporting USCIS mission systems.",
    ),
    "ula": (
        "United Launch Alliance (Vulcan Rocket Program)",
        "Cybersecurity Architect leading 28-person team. First-ever CNSSI 1253 assessment "
        "and concurrent DCMA/ISO recertification for national security space program.",
        "Zero audit findings. Established repeatable evidence and policy management program adopted program-wide.",
    ),
    "corporate": (
        "Corporate Tools / NW Registered Agent",
        "Security Engineering Manager. AI-powered security automation, CI/CD security review, "
        "SOC 2 Type 1 readiness, and PCI DSS v4.0.1 compliance environment.",
        "700+ accounts analyzed across 11 fraud investigations. Automated evidence collection reduced audit prep time significantly.",
    ),
    "navy": (
        "U.S. Navy — Combat Systems (2000–2010)",
        "Fire Controlman, Data Systems Technician, Combat Systems Supply Officer. "
        "$22M+ defense procurement management. Security clearance holder.",
        "10 years service. DoD mission, procurement, and federal compliance culture expertise.",
    ),
}

MARKETS = {
    # ─────────────────────────────────────────────────────────────────────────
    "Federal": {
        "filename": "Waypoint_CapStmt_Federal.pdf",
        "tagline": "FedRAMP 20x, FISMA & Cybersecurity Compliance for Federal Agencies",
        "overview": (
            "Waypoint Compliance Advisory is an SBA-certified Service-Disabled Veteran-Owned Small Business delivering "
            "FedRAMP, FISMA, and cybersecurity compliance services to federal agencies and cloud service providers. "
            "With direct experience inside HHS OIG and DHS/USCIS, we understand what federal compliance looks like from "
            "the inside, not just from reading the framework. 21+ years of hands-on federal security experience means "
            "we know what auditors actually check."
        ),
        "competencies": [
            ("FedRAMP 20x Advisory",
             "Authorization readiness under the 20x model and CR26 rulesets, Key Security Indicators, continuous "
             "validation, and machine-readable evidence for CSPs seeking federal agency ATO."),
            ("FedRAMP Rev 5 Transition",
             "Machine-readable authorization package conversion ahead of the September 30, 2026 deadline, plus "
             "transition planning before Rev 5 applications close June 11, 2027."),
            ("FISMA & NIST RMF",
             "System categorization, control selection and implementation, FISMA ATO package development, and ongoing "
             "RMF monitoring for civilian federal systems."),
            ("AI Security & Governance",
             "AI risk assessments, governance framework development aligned to NIST AI RMF and OMB AI policy, secure AI "
             "implementation, and AI supply chain security reviews."),
            ("Security Architecture & Assessment",
             "Zero trust architecture design, DISA STIG compliance, NIST 800-53 Rev 5 control gap analysis, and security "
             "architecture review for federal IT environments."),
            ("Fractional vCISO — Federal",
             "Ongoing security leadership for federal contractors and agencies. Policy development, risk governance, "
             "ATO maintenance, and continuous compliance management."),
        ],
        "pp_order": ["hhs", "uscis", "ula", "corporate", "navy"],
        "why": [
            ("SDVOSB Set-Aside Eligible",
             "Competitive advantage on VA, DoD, and civilian federal set-aside vehicles. SBA certified SDVOSB, App #63605."),
            ("Agency Insider Perspective",
             "Direct HHS OIG and USCIS/DHS experience. We know what federal auditors actually look for, including the gaps "
             "that consistently get missed by outside consultants."),
            ("Current on a Moving Target",
             "FedRAMP 20x, the Rev 5 machine-readable mandate, and CMMC reform are all in motion right now. We track "
             "the rule changes so your authorization strategy is built on what is actually in effect."),
            ("Builder, Not Just Auditor",
             "Delivers automated evidence systems, policy libraries, and continuous monitoring tooling that make federal "
             "compliance sustainable beyond the ATO milestone."),
        ],
        "teaming": [
            ("Subcontracting Available",
             "Available to federal IT prime contractors as a specialized security and compliance subcontractor. SDVOSB "
             "status supports your small business subcontracting goals."),
            ("Teaming Partners Welcome",
             "Actively seeking teaming arrangements with systems integrators, CDM program primes, and cloud service "
             "providers pursuing FedRAMP 20x authorization."),
            ("Engagement Model",
             "Fixed-price FedRAMP 20x readiness assessments and FISMA ATO packages. Fractional vCISO retainers "
             "($4K–$8K/month). ConMon and ongoing compliance support available."),
            ("Clearance Background",
             "Founder holds prior clearance history and 10-year Navy service background. Available for sensitive "
             "environments with appropriate sponsorship."),
        ],
    },
    # ─────────────────────────────────────────────────────────────────────────
    "Defense": {
        "filename": "Waypoint_CapStmt_Defense.pdf",
        "tagline": "NIST 800-171, DFARS & CUI Protection for the Defense Industrial Base",
        "overview": (
            "Waypoint Compliance Advisory is an SBA-certified Service-Disabled Veteran-Owned Small Business helping "
            "defense contractors meet the CUI protection obligations already written into their contracts. DFARS "
            "252.204-7012 and NIST SP 800-171 apply today, independent of any certification program. A weak or "
            "undocumented SPRS score is a contract and False Claims Act risk right now. We build the security program "
            "and evidence that satisfies current requirements and carries directly into third-party certification if "
            "and when DoD resumes CMMC Phase 2."
        ),
        "competencies": [
            ("NIST 800-171 Self-Assessment",
             "Full 110-control assessment scored to the DoD assessment methodology, with the objective evidence needed "
             "to defend the score you post to SPRS."),
            ("SPRS Score Remediation",
             "Prioritized remediation of the controls costing you the most points, sequenced by score impact per dollar "
             "so a low score becomes a credible one before your next award."),
            ("SSP & POA&M Development",
             "System security plans and plans of action that hold up under government review. This is the documentation DFARS "
             "assumes you already maintain."),
            ("CUI Scoping & Supply Chain",
             "CUI identification and enclave scoping to shrink your assessment boundary, plus subcontractor flow-down "
             "management and supply chain risk assessment."),
            ("Incident Response & DFARS Reporting",
             "IR plans, tabletop exercises, and 72-hour cyber incident reporting procedures that satisfy DFARS "
             "252.204-7012 (c) through (g)."),
        ],
        "pp_order": ["ula", "navy", "hhs", "uscis", "corporate"],
        "why": [
            ("Requirements That Are Real Today",
             "DoD suspended CMMC Phase 2 third-party certification in July 2026. Your DFARS 7012 and NIST 800-171 "
             "obligations did not change. We focus your budget on what is actually enforceable."),
            ("SDVOSB Set-Aside Eligible",
             "Competitive advantage on DoD set-aside vehicles and prime small business subcontracting goals. SBA "
             "certified SDVOSB, App #63605."),
            ("National Security Program Experience",
             "Led the first-ever CNSSI 1253 assessment for the ULA Vulcan rocket program with zero audit findings. "
             "10 years U.S. Navy combat systems and $22M+ defense procurement."),
            ("Certification-Ready by Design",
             "Every control we implement is documented to assessment standard. If Phase 2 resumes, you are not starting "
             "over. You are scheduling an assessment."),
        ],
        "teaming": [
            ("Subcontracting Available",
             "Available to defense primes as a specialized security and compliance subcontractor. SDVOSB status "
             "supports your small business subcontracting plan goals."),
            ("Flow-Down Support for Primes",
             "Assess and remediate your subcontractor base. Supply chain risk management and DFARS flow-down "
             "verification across multi-tier supplier networks."),
            ("Engagement Model",
             "Fixed-price NIST 800-171 self-assessments with SPRS-ready scoring packages. Remediation sprints and "
             "fractional vCISO retainers ($4K–$8K/month)."),
            ("Clearance Background",
             "Founder holds prior clearance history and 10-year Navy service background. Available for sensitive "
             "environments with appropriate sponsorship."),
        ],
    },
    # ─────────────────────────────────────────────────────────────────────────
    "Healthcare": {
        "filename": "Waypoint_CapStmt_Healthcare.pdf",
        "tagline": "HIPAA Security, Risk Assessment & ePHI Protection for Healthcare",
        "overview": (
            "Waypoint Compliance Advisory is an SBA-certified Service-Disabled Veteran-Owned Small Business delivering "
            "HIPAA Security Rule compliance to covered entities, business associates, and health IT organizations. The "
            "annual Security Risk Assessment required by 45 CFR 164.308(a)(1)(ii)(A) is the single most common finding "
            "in HHS OCR enforcement actions. With direct HHS Office of Inspector General experience, we know what "
            "federal healthcare auditors actually check, and what a defensible assessment looks like."
        ),
        "competencies": [
            ("HIPAA Security Risk Assessment",
             "Comprehensive SRA aligned to 45 CFR 164.308, covering administrative, physical, and technical safeguards. "
             "Gap identification, risk ranking, and audit-ready evidence documentation."),
            ("Policy & Procedure Development",
             "HIPAA-compliant security policies, workforce training programs, sanction policies, and administrative "
             "safeguard documentation that survives OCR review."),
            ("Breach Notification & Incident Response",
             "Breach risk assessment procedures, 60-day notification workflows under the Breach Notification Rule, IR "
             "plans, and healthcare-specific tabletop exercises."),
            ("ePHI Security Architecture",
             "Health IT security architecture, access control and audit logging design, encryption strategy, and "
             "medical device / IoT network segmentation."),
            ("Business Associate Compliance",
             "BAA review and gap analysis, vendor risk assessment, and downstream subcontractor compliance for "
             "organizations serving covered entities."),
        ],
        "pp_order": ["hhs", "corporate", "uscis", "ula", "navy"],
        "why": [
            ("HHS OIG Insider Perspective",
             "Lead Security Engineer inside the HHS Office of Inspector General across 13 production teams implementing "
             "the HIPAA Security Rule. We have been on the government side of healthcare security."),
            ("Annual Requirement, Recurring Partner",
             "The SRA is not a one-time project. We build assessment and evidence programs designed to be repeated "
             "efficiently every year rather than rebuilt from scratch."),
            ("Current on the Proposed Rewrite",
             "The January 2025 Security Rule NPRM would remove the addressable/required distinction and mandate MFA, "
             "encryption, and asset inventory. Final action is now expected in 2027. We assess against today's rule "
             "while flagging where the proposal would move the bar."),
            ("Beyond the Checklist",
             "Risk assessments that identify real exposure in your environment, not a template with your logo on it. "
             "Findings are ranked by actual likelihood and patient data impact."),
            ("Builder, Not Just Auditor",
             "Delivers automated evidence collection, policy libraries, and continuous monitoring tooling that keep you "
             "audit-ready between assessments."),
        ],
        "teaming": [
            ("Who We Serve",
             "Physician practices, hospitals and health systems, behavioral health providers, dental groups, health IT "
             "and digital health companies, billing and RCM firms, and other business associates."),
            ("Subcontracting & Partnerships",
             "Available to health IT integrators, MSPs, and healthcare consulting firms needing HIPAA security "
             "expertise. Referral partnerships welcome with healthcare legal and accounting practices."),
            ("Engagement Model",
             "Fixed-price annual HIPAA Security Risk Assessments. Policy and IR plan development packages. Fractional "
             "vCISO retainers ($4K–$8K/month) for ongoing security leadership."),
            ("Federal Healthcare Programs",
             "SDVOSB set-aside eligible for VA, HHS, and Medicaid-related federal and state health program contracts."),
        ],
    },
    # ─────────────────────────────────────────────────────────────────────────
    "State": {
        "filename": "Waypoint_CapStmt_State.pdf",
        "tagline": "Cybersecurity Compliance for Florida State & Local Government",
        "overview": (
            "Waypoint Compliance Advisory is an SBA-certified Service-Disabled Veteran-Owned Small Business and "
            "registered Florida MyFloridaMarketPlace vendor delivering cybersecurity compliance services to state "
            "agencies, counties, municipalities, school districts, and public health programs. As a certified Florida "
            "Veteran Business Enterprise, we are set-aside eligible for state procurement. 21+ years of federal and "
            "commercial security experience, applied to public sector budgets and timelines."
        ),
        "competencies": [
            ("NIST CSF 2.0 Assessment & Roadmap",
             "Cybersecurity maturity baseline against NIST CSF 2.0, including the Govern function added in the 2.0 "
             "release, with a prioritized, budget-aware remediation roadmap suitable for legislative and board "
             "reporting."),
            ("Security Program Development",
             "Build or mature an agency security program end to end: governance structure, policies and procedures, "
             "control implementation, and workforce training."),
            ("HIPAA for State Health Programs",
             "Security risk assessments and Security Rule compliance for Medicaid, county health departments, and "
             "state-run healthcare and behavioral health programs."),
            ("Incident Response & Continuity",
             "IR plans, tabletop exercises, ransomware preparedness, and continuity of operations planning for public "
             "sector environments and critical citizen services."),
            ("Fractional vCISO — Public Sector",
             "Executive security leadership for agencies that need strategic direction, procurement support, and "
             "compliance oversight without a full-time CISO line item."),
        ],
        "pp_order": ["hhs", "uscis", "corporate", "ula", "navy"],
        "why": [
            ("Florida Procurement Ready",
             "Registered MyFloridaMarketPlace vendor and certified Florida Veteran Business Enterprise / Certified "
             "Business Enterprise. Set-aside eligible and ready to contract."),
            ("Federal Rigor, Public Sector Budgets",
             "HHS OIG and DHS/USCIS experience brought to state and local agencies, delivering federal-grade assessment quality "
             "scoped and priced for public sector realities."),
            ("Local Presence",
             "Based in DeLand, Florida. On-site availability for Central Florida agencies, districts, and "
             "municipalities without travel line items."),
            ("Builder, Not Just Auditor",
             "Delivers automated evidence systems, policy libraries, and monitoring tooling so small agency IT teams "
             "can sustain compliance without added headcount."),
        ],
        "teaming": [
            ("Who We Serve",
             "State agencies, county and municipal government, school districts and higher education, public health "
             "and Medicaid programs, utilities and special districts."),
            ("Subcontracting & Teaming",
             "Available to state IT primes and integrators as a specialized security and compliance subcontractor. "
             "VBE/CBE status supports diversity and veteran participation requirements."),
            ("Engagement Model",
             "Fixed-price NIST CSF 2.0 assessments and security program builds. Fractional vCISO retainers "
             "($4K–$8K/month). Purchasable through MFMP and state term contract vehicles."),
            ("Grant & Funding Support",
             "Assessment documentation structured to support State and Local Cybersecurity Grant Program applications "
             "and other public sector cybersecurity funding requests."),
        ],
    },
}
