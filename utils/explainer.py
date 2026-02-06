def explain_clause(clause: str, language: str = "English") -> str:
    clause_lower = clause.lower()

    explanations = {
        "unlimited liability": "This clause exposes one party to unlimited financial loss.",
        "non-compete": "This clause restricts your ability to work with competitors.",
        "auto-renew": "This clause automatically renews the contract unless cancelled.",
        "termination without notice": "This allows termination without prior warning.",
        "indemnify": "This requires one party to cover legal losses of the other.",
        "intellectual property": "This determines who owns work created under the contract."
    }

    for key, explanation in explanations.items():
        if key in clause_lower:
            return explanation if language == "English" else f"(Hindi) {explanation}"

    return (
        "This clause does not appear to carry significant legal risk."
        if language == "English"
        else "इस अनुच्छेद में कोई बड़ा कानूनी जोखिम नहीं पाया गया।"
    )
