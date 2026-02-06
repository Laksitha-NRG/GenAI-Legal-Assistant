import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    doc = nlp(text)
    entities = {
        "Parties (ORG)": [],
        "Dates": [],
        "Money": [],
        "Location/Jurisdiction": []
    }

    for ent in doc.ents:
        if ent.label_ == "ORG":
            entities["Parties (ORG)"].append(ent.text)
        elif ent.label_ == "DATE":
            entities["Dates"].append(ent.text)
        elif ent.label_ == "MONEY":
            entities["Money"].append(ent.text)
        elif ent.label_ in ["GPE", "LOC"]:
            entities["Location/Jurisdiction"].append(ent.text)

    return entities
