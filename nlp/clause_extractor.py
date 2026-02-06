import re

def extract_clauses(text):
    clauses = re.split(r'\n\d+\.|\nClause\s\d+', text)
    return [c.strip() for c in clauses if len(c.strip()) > 40]
