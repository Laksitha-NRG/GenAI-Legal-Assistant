from langdetect import detect

def detect_language(text):
    """
    Detects language of input text.
    Returns:
    'hi' -> Hindi
    'en' -> English
    'unknown' -> Detection failed
    """
    try:
        return detect(text)
    except:
        return "unknown"
