import os

# Chemins
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "passenger_stress_data.csv")

# Modèle BERT multilingue pré-entrainé pour le sentiment (1 à 5 étoiles)
# Ce modèle "nlptown" est très performant sur FR, EN, AR, ES, DE
MODEL_NAME = "nlptown/bert-base-multilingual-uncased-sentiment"

# RÈGLE MÉTIER : Conversion Sentiment (Étoiles) -> Stress RAM
# 1-2 étoiles (Négatif) = Stress Fort
# 3 étoiles (Neutre)    = Stress Moyen
# 4-5 étoiles (Positif) = Stress Faible
LABELS_MAPPING = {
    "1 star": "Stress_fort",
    "2 stars": "Stress_fort",
    "3 stars": "Stress_moyen",
    "4 stars": "Stress_faible",
    "5 stars": "Stress_faible"
}