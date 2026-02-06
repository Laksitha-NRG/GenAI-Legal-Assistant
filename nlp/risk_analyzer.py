def analyze_clause_risk(clause: str) -> str:
    clause_lower = clause.lower()

    high_risk_keywords = [
        "unlimited liability",
        "without limitation",
        "non-compete",
        "non compete",
        "exclusive",
        "indemnify",
        "indemnification",
        "penalty",
        "termination without notice",
        "sole discretion",
        "perpetual",
        "irrevocable",
        "ownership of all intellectual property"
    ]

    medium_risk_keywords = [
        "auto-renew",
        "automatic renewal",
        "confidentiality",
        "governing law",
        "jurisdiction",
        "liquidated damages",
        "notice period",
        "intellectual property",
        "warranty",
        "limitation of liability"
    ]

    for word in high_risk_keywords:
        if word in clause_lower:
            return "HIGH"

    for word in medium_risk_keywords:
        if word in clause_lower:
            return "MEDIUM"

    return "LOW"

