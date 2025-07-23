# 🧠 Article Verification System

Un système intelligent de vérification automatique des articles basé sur FastAPI, MongoDB et des modèles d'apprentissage automatique (CatBoost, XGBoost, etc.). Ce système permet de détecter des anomalies dans les articles collectés via une API externe, comme les duplications, champs vides, ou valeurs incohérentes.

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
```bash

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
👉 http://127.0.0.1:8000

📬 **Routes disponibles**
GET /articles/articles : Vérifie les articles de la base de données

POST /articles/testarticle : Vérifie des articles provenant d'une API externe

✅ **Exemple d'appel API**
```bash
curl -X POST http://localhost:8000/articles/testarticle
```

👨‍💻 **Auteur**
Helmi Soudana – @Helmisoudana