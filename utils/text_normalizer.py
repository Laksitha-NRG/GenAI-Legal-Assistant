from langdetect import detect

def normalize_contract_text(text):
    """
    Detects language and normalizes text.
    Returns:
      normalized_text, detected_language
    """

    try:
        detected_lang = detect(text)
    except:
        detected_lang = "en"

    # Hindi → keep Hindi (do NOT translate here)
    if detected_lang == "hi":
        return text, "Hindi"

    # Default English
    return text, "English"

