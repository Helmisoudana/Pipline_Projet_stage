from loguru import logger
import sys
import os
from datetime import datetime

# Crée un dossier "logs" s'il n'existe pas
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Nom du fichier log (avec horodatage)
log_filename = os.path.join(LOG_DIR, f"{datetime.now():%Y-%m-%d}.log")

# Nettoyer les handlers existants pour éviter les doublons
logger.remove()

# Ajouter console (stdout)
logger.add(sys.stdout, level="INFO", format="<green>{time:HH:mm:ss}</green> | <level>{level}</level> | <cyan>{message}</cyan>")

# Ajouter fichier avec rotation quotidienne et conservation
logger.add(log_filename, 
           rotation="00:00",          # rotation chaque jour à minuit
           retention="7 days",        # garder les logs 7 jours
           level="DEBUG",             # niveau minimal à logger dans le fichier
           format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}")

# Exemple d’utilisation
if __name__ == "__main__":
    logger.info("Logger configuré correctement.")
    logger.warning("Ceci est un avertissement.")
    logger.error("Ceci est une erreur.")
