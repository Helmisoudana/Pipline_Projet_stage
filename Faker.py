from faker import Faker
from datetime import datetime
import random
from models.article import article
from sqlmodel import select
from models.arfamille import arfamille
from models.ar_sfamille import ar_sfamille
from models.saison import saison
from models.fournisseur import fournisseur
from models.ar_couleur import ar_couleur
from models.grille import grille
from database.session import get_session
from database.session import get_session
import string
from datetime import timedelta


fake = Faker('fr_FR')

# Nombre d'articles à générer
NB_ARTICLES = 50
def extraire_lettre_saison(saison_str: str) -> str:
    saison_str = saison_str.upper()  # Pas de lettre de saison
    if "HIVER" in saison_str:
        return "H"
    elif "ETE" in saison_str:
        return "E"
    return ""  # Valeur par défaut en cas de doute


def get_all_ids_with_extra(session):
    familles = session.exec(select(arfamille)).all()
    sous_familles = session.exec(select(ar_sfamille)).all()
    saisons = session.exec(select(saison)).all()
    grilles = session.exec(select(grille)).all()
    fournisseurs = session.exec(select(fournisseur)).all()
    Couleurs=session.exec(select(ar_couleur)).all()

    return familles, sous_familles, saisons, grilles ,fournisseurs, Couleurs

def generate_code(ordre, famille_libelle,Saison):
    saisonletter=extraire_lettre_saison(Saison)
    digits = ''.join(random.choices(string.digits, k=4))
    optional_letter = random.choice(string.ascii_uppercase) if random.random() < 0.5 else ''
    return f"{ordre}{saisonletter}N{famille_libelle}{digits}{optional_letter}"

def insert_fake_articles():
    with get_session() as session:
        familles, sous_familles, saisons, grilles , fournisseurs , Couleurs = get_all_ids_with_extra(session)

        articles = []
        for _ in range(NB_ARTICLES):
            famille = random.choice(familles)
            sous_famille = random.choice(sous_familles)
            saison_obj = random.choice(saisons)
            grille_obj = random.choice(grilles)
            fournisseur_obj=random.choice(fournisseurs)
            couleur_obj=random.choice(Couleurs)

            prix_achat = round(random.uniform(10, 50), 2)
            prix_fac = round(prix_achat * random.uniform(2.0, 3.7), 2)

            now = datetime.now()
            code = generate_code(saison_obj.Ordre, famille.Code, saison_obj.Saison)

            art = article(
                Article=fake.word().capitalize(),
                Code=code,
                PrixFac=prix_fac,
                prixAchat=prix_achat,
                Etat=random.choice([1, 2,3]),
                IDArFamille=famille.IDArFamille,
                IDArSousFamille=sous_famille.IDArSousFamille,
                IDSaison=saison_obj.IDSaison,
                IDFournisseur=fournisseur_obj.IDFournisseur,
                IDAr_Couleur=couleur_obj.IDAr_Couleur,
                IDGrille=grille_obj.IDGrille,
                numInterne=fake.unique.random_number(digits=5),
                SaisiLe=now,
                ModifieLe=now + timedelta(minutes=random.randint(1, 60)),
            )
            articles.append(art)
        session.add_all(articles)
        session.commit()
        print(f"{NB_ARTICLES} articles générés et insérés avec succès.")

if __name__ == "__main__":
    insert_fake_articles()