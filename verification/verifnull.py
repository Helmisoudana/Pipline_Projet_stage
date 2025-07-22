def detect_null_or_vide_champs(articles: list[dict]) -> list[dict]:
    anomalies = []
    values=''
    for article in articles:
        for field, value in article.items():

            if field == "SousFamille":
                continue

            # On considère comme vide : None, '', 'null', 'NULL', '   '
            if value is None or str(value).strip().lower() in ['', 'null' , '0']:
                values+= ' ' + str(field) 
        if values != '' :     
            anomalies.append({
                    'IDArticle': article.get('IDArticle'),
                    'Type': 'champ_vide',
                    'Code': article.get('Code'),
                    'message': f"Champs {values} est vide ou null pour l'article ID {article.get('IDArticle')} et verifiez le code s'il vous plais"
                })
            values=''           
    return anomalies
