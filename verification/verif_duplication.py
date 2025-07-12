import json

def detect_duplicates(articles):
    seen = set()
    anomalies = []

    for article in articles:
        # Convertit chaque article (dictionnaire) en chaîne JSON ordonnée pour comparaison
        article_str = json.dumps(article, sort_keys=True)

        if article_str in seen:
            anomalies.append({
                'IDArticle': article['IDArticle'],
                'Type': 'duplication_complete',
                'Code' :article['Code'],
                'message': "Article entièrement dupliqué"
            })
        else:
            seen.add(article_str)

    return anomalies
