def explain_clause(clause, language="English"):
    """
    Returns a simple legal explanation of a clause
    in English or Hindi based on detected language.
    """

    if language == "Hindi":
        return (
            "यह क्लॉज अनुबंध की एक महत्वपूर्ण शर्त को दर्शाता है। "
            "यह बताता है कि पक्षों के अधिकार और जिम्मेदारियाँ क्या हैं। "
            "यदि यह शर्त एकतरफा है या स्पष्ट नहीं है, "
            "तो इससे व्यवसाय को कानूनी या वित्तीय नुकसान हो सकता है।"
        )

    # Default: English
    return (
        "This clause explains an important contractual condition. "
        "It outlines the rights and obligations of the parties involved. "
        "If the terms are unclear or one-sided, it may pose legal or financial risk."
    )
