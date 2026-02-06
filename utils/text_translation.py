from indic_transliteration.sanscript import transliterate
from indic_transliteration import sanscript

def hindi_to_english(text):
    """
    Converts Hindi (Devanagari) text to Romanized English.
    """
    return transliterate(text, sanscript.DEVANAGARI, sanscript.ITRANS)
