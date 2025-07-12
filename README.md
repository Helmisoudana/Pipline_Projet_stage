# 🎯 Pipeline de Vérification d'Articles

Ce projet est un **pipeline d'analyse automatique** des articles commerciaux, qui détecte plusieurs types d’anomalies :
- Champs vides
- Duplications
- Erreurs de code
- Anomalies détectées via modèle Machine Learning (scikit-learn)

Les articles sont récupérés via une API et les anomalies sont enregistrées dans une base de données SQL.

---

## 📁 Structure du projet
NafNafSystem/
│
├── main.py # Démarrage FastAPI et scheduler
├── verification/
│ ├── pipline.py # Exécution du pipeline complet
│ ├── fetchdata.py # Récupération des articles depuis une API
│ ├── fetchdata_withJson.py # Récupération via JSON POST
│ ├── verif_duplication.py # Détection de doublons
│ ├── verifnull.py # Détection de champs vides
│ ├── VerifCode.py # Vérification des formats de code
│ └── detect_avec_model.py # Détection via modèle ML
│
├── models/ # Modèles SQLModel (Article, Anomalie, etc.)
├── database/ # Configuration de la session SQLModel
│
├── .env # Variables d’environnement
├── requirements.txt # Dépendances Python
└── README.md # Ce fichier

---

## 🚀 Comment exécuter le projet

### 1. Cloner le dépôt
2. Créer un environnement virtuel
bash
Copier
Modifier
python -m venv venv
# Linux/macOS
source venv/bin/activate
# Windows
venv\Scripts\activate
3. Installer les dépendances
bash
Copier
Modifier
pip install -r requirements.txt
⚙️ Configuration .env
Crée un fichier .env à la racine du projet avec le contenu suivant :

env
Copier
Modifier
API_URL=http://127.0.0.1:8000/article/
API_URL_BY_ID=http://127.0.0.1:8000/article/by_ids
MONGODB_URL=mongodb://localhost:27017
MYSQL_URL=mysql+mysqlconnector://root:password@localhost:3306/nom_de_ta_base
🔧 Remplace password et nom_de_ta_base par les valeurs de ta configuration locale.

🧠 Technologies utilisées
FastAPI – Framework web rapide pour APIs

SQLModel – ORM basé sur SQLAlchemy + Pydantic

APScheduler – Exécution automatique du pipeline périodiquement

Scikit-learn – Modèle de détection d’anomalies

pymongo – Connexion MongoDB (optionnel)

requests – Requêtes HTTP vers API distante

python-dotenv – Gestion des variables d’environnement

▶️ Lancer l'application
bash
Copier
Modifier
uvicorn main:app --reload
Démarre le serveur FastAPI et le scheduler (le pipeline s’exécute toutes les 2 heures automatiquement).

🧪 Endpoints utiles
Méthode	URL	Description
POST	/article/import	Importation par JSON (liste d'IDs)
GET	/article/	Récupère tous les articles disponibles
POST	/pipeline/run	Lance manuellement le pipeline

✍️ Auteur
Helmi Soudana
📍 ENISo, Tunisie
📧 helmi.soudana@example.com

