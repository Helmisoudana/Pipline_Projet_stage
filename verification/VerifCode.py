import re

def extraire_lettre_saison(saison_str: str) -> str:
    saison_str = saison_str.upper()  # Pas de lettre de saison
    if "HIVER" in saison_str:
        return "H"
    elif "ETE" in saison_str:
        return "E"
    return ""  # Valeur par défaut en cas de doute

def is_saison_permanent(saison_str: str) -> bool:
    return "PERMANENT" in saison_str.upper()

def detect_code_errors(articles):
    anomalies = []

    for article in articles:
        code = article.get("Code", "")
        ordre = (article.get("Ordre", "") or "").strip().upper() or ""
        saison = (article.get("Saison", "") or "").strip().upper() or ""
        saison_lettre = extraire_lettre_saison(saison)
        famille_lettre = (article.get("codeFamille", "") or "").strip().upper() or ""

        if is_saison_permanent(saison):
            # En cas de saison permanente → lettre de saison optionnelle
            pattern = f"^{ordre}N{famille_lettre}\\d+[A-Z]?$"
        else:
            # Sinon → lettre obligatoire
            pattern = f"^{ordre}{saison_lettre}N{famille_lettre}\\d+[A-Z]?$"

        if not re.fullmatch(pattern, code):
            anomalies.append({
                "IDArticle": article.get("IDArticle"),
                "Type" : 'Code incorrecte',
                "Code": code,
                "message": f"Le code ne correspond pas à la structure attendue le Pattern attendu est'{pattern}' "
            })

    return anomalies
