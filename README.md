📄 README.md
markdown
Copier
Modifier
# 🎯 Pipeline de Vérification d'Articles

Ce projet est un **pipeline d'analyse automatique** des articles commerciaux, qui détecte plusieurs types d’anomalies (champs vides, duplication, erreurs de code, anomalies via modèle ML) à partir de données d’articles récupérées via une API. Les anomalies détectées sont enregistrées dans une base de données SQL.

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

yaml
Copier
Modifier

---

## 🚀 Comment exécuter le projet

### 1. Cloner le dépôt

```bash
git clone https://github.com/Helmisoudana/Pipline_Projet_Stage.git
cd Pipline_Projet_Stage
2. Créer un environnement virtuel
bash
Copier
Modifier
python -m venv venv
source venv/bin/activate          # Linux/macOS
venv\Scripts\activate             # Windows
3. Installer les dépendances
bash
Copier
Modifier
pip install -r requirements.txt
⚙️ Configuration .env
Crée un fichier .env à la racine du projet (s’il n’existe pas) et ajoute :

env
Copier
Modifier
API_URL=http://127.0.0.1:8000/article/
API_URL_BY_ID=http://127.0.0.1:8000/article/by_ids
MONGODB_URL=mongodb://localhost:27017
MYSQL_URL=mysql+mysqlconnector://root:password@localhost:3306/nom_de_ta_base
🛠 Remplace password et nom_de_ta_base selon ta config locale.

🧠 Technologies utilisées
FastAPI – Framework API web rapide

SQLModel – ORM basé sur SQLAlchemy et Pydantic

APScheduler – Exécution périodique du pipeline

Scikit-learn – Pour le modèle de détection d'anomalies

pymongo – Accès à MongoDB (optionnel)

requests – Requêtes HTTP vers API

python-dotenv – Chargement des variables d’environnement

▶️ Lancer l'application
bash
Copier
Modifier
uvicorn main:app --reload
Cela démarre le serveur FastAPI et le scheduler du pipeline toutes les 2 heures.

🧪 Endpoints utiles
Méthode	URL	Description
POST	/article/import	Importation par JSON (liste d'IDs)
GET	/article/	Récupère tous les articles
POST	/pipeline/run	Lance manuellement le pipeline

✍️ Auteur
Helmi Soudana
📍 ENISo, Tunisie
📧 helmi.soudana@example.com

📜 Licence
Ce projet est open-source sous licence MIT.

yaml
Copier
Modifier

---

Souhaite-tu que je crée le fichier et le pousse dans ton dépôt GitHub automatiquement (en t'expliquant comment faire), ou préfères-tu le faire manuellement ?








Demander à ChatGPT
