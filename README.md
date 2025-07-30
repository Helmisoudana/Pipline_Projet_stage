# 🧠 Article Verification System

`🧠 Description du Système Intelligent de Détection d’Anomalies`:

Article Verification System est un système intelligent conçu pour automatiser la détection d’anomalies dans une base de données d’articles à l’aide d’un modèle de machine learning intégré. 

`⚙️ Fonctionnalités principales`

Détection intelligente d’anomalies :

Le système intègre un modèle de machine learning entraîné pour détecter automatiquement les incohérences ou anomalies sur les articles (champs incohérents, valeurs extrêmes, duplications, etc.).

Surveillance quotidienne automatique :
Un service planifié s’exécute toutes les 24 heures afin de :

- Identifier tous les articles créés ou modifiés la veille.

- Transmettre ces articles au module de détection pour analyse.

- Enregistrer les anomalies détectées dans la base de données dédiée.

Double API FastAPI :

- `get "/VerifierByIds"` : Une API REST qui reçoit une liste d’IDs d’articles, les récupère depuis la base de données principale, et les soumet au système de détection.

- `POST "/TestArticle"` : Une API de test permettant de soumettre manuellement des articles (au format JSON) pour tester la robustesse du système sans modifier la base de production.



## 📁 Structure du projet
```bash
+---database
|   |   session.py
|   |
|   \---__pycache__
|           session.cpython-310.pyc
|
+---logs
|       2025-07-22.log
|       2025-07-23.log
|
+---ml_model
|       catboost_model.cbm
|       famille_sf_mapping.json
|
+---models
|   |   anomalie.py
|   |   arfamille.py
|   |   article.py
|   |   ar_couleur.py
|   |   ar_sfamille.py
|   |   codebarre.py
|   |   fournisseur.py
|   |   grille.py
|   |   saison.py
|   |   tailles.py
|   |
|   \---__pycache__
|           anomalie.cpython-310.pyc
|           arfamille.cpython-310.pyc
|           article.cpython-310.pyc
|           ar_couleur.cpython-310.pyc
|           ar_sfamille.cpython-310.pyc
|           codebarre.cpython-310.pyc
|           fournisseur.cpython-310.pyc
|           grille.cpython-310.pyc
|           saison.cpython-310.pyc
|
+---routes
|   |   article_routes.py
|   |   verifierArticles_routes.py
|   |
|   \---__pycache__
|           article_routes.cpython-310.pyc
|           verifierArticles_routes.cpython-310.pyc
|
+---schemas
|   |   article_schema.py
|   |   response_schema.py
|   |
|   \---__pycache__
|           article_schema.cpython-310.pyc
|           response_schema.cpython-310.pyc
|
+---services
|   |   pipline.py
|   |   pipline_API.py
|   |
|   \---__pycache__
|           pipline.cpython-310.pyc
|           pipline_API.cpython-310.pyc
|
+---tests
|       Faker.py
|       test.py
|
+---utils
|   |   logger.py
|   |
|   \---__pycache__
|           logger.cpython-310.pyc
|
\---verification
    |   detect_avec_model.py
    |   fetchdata.py
    |   fetchdata_withJson.py
    |   piplineTestArticle.py
    |   save_anomalies.py
    |   VerifCode.py
    |   verifnull.py
    |   verif_duplication.py
```

## 🚀 Fonctionnalités

- 🔍 **Analyse intelligente des articles** en 3 étapes :
  - `verif1`: détection des doublons
  - `verif2`: détection des champs vides critiques
  - `verif2`: détection des Code Articles
  - `verif4`: détection de valeurs aberrantes
- 🔍 Analyse intelligente d’articles via un modèle ML (CatBoost)
- 📦 Gestion des articles via une API RESTful
- 🧠 Détection d’anomalies automatisée (valeurs manquantes, marges incohérentes, duplications…)
- 🌐 Interface web intuitive pour visualiser les résultats
- 🗃️ Persistance des anomalies dans MYSQL
- 🧪 API REST avec FastAPI pour déclencher les vérifications
- 🧠 Architecture modulaire et évolutive

## 🛠️ Installation

1. **Cloner le projet** :
```bash
git clone https://github.com/Helmisoudana/Pipline_Projet_stage
cd NafNafSystem
```
2. **Créer un environnement virtuel** :
```bash
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate sur Windows
```
3. **Installer les dépendances** :
```bash
pip install -r requirements.txt
```
4. **Configurer .env** :
Assurez-vous que votre fichier .env contient l'URI MYSQL et les paramètres nécessaires.

5. **Lancer le projet** :
```bash
uvicorn main:app --reload
```
Ouvrir dans le navigateur :
👉 http://127.0.0.1:8000 : par defaut

📬 **Routes disponibles** 

`GET "/VerifierByIds"`: Vérifie les articles de la base de données

`POST "/testarticle"` : Vérifie des articles provenant d'une API externe

✅ **Exemple d'appel API**
```bash
curl -X POST http://localhost:8000/testarticle
```
📚 **Visualiser la documentation de l'API**

🔹 **Option 1 : Aperçu local avec l'extension VS Code**

1. Installe l'extension Swagger Viewer :
   - Ouvre Visual Studio Code.
   - Va dans les extensions (Ctrl + Shift + X).
   - Recherche **Swagger Viewer** et installe-la.
2. Ouvre le fichier `API-Doc.yaml` ou `API-Doc.json`.
3. Clique droit > **Preview Swagger**  
   ou appuie sur Ctrl + Shift + P, tape **Swagger: Preview**.

---

🔹 **Option 2 : Via Swagger UI intégré (FastAPI)**

Lance le serveur FastAPI, puis accède à la documentation interactive :  
`http://localhost:${port}/docs`

---

🔹 **Option 3 : Visualiser un fichier local avec Swagger UI**

Tu as un fichier `API-Doc.json` :  
1. Va sur [https://editor.swagger.io](https://editor.swagger.io)  
2. Clique sur **File > Import File** et charge ton fichier local.

---

👨‍💻 Auteur Helmi Soudana – @Helmisoudana