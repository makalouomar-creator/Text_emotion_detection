import pandas as pd
from sklearn.metrics import classification_report, accuracy_score
from src.stress_inference import get_stress_from_text
import time

def evaluate_model(csv_path="data/passenger_stress_data.csv"):
    print(f"📂 Chargement des données depuis {csv_path}...")
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        print("❌ Erreur : Fichier CSV introuvable. Lance 'create_dataset.py' d'abord.")
        return

    print(f"🔄 Lancement de l'inférence sur {len(df)} phrases...")
    
    y_true = df["stress_label"].tolist()
    y_pred = []
    
    start_time = time.time()
    
    # Boucle sur chaque texte pour prédire le stress
    for i, text in enumerate(df["text"]):
        # Petit indicateur de progression
        if i % 5 == 0:
            print(f"   Traitement ligne {i}/{len(df)}...", end="\r")
            
        result = get_stress_from_text(text)
        y_pred.append(result["stress_level"])

    duration = time.time() - start_time
    print(f"✅ Inférence terminée en {duration:.2f} secondes.\n")

    # Calcul des métriques
    print("--- 📊 RAPPORT DE PERFORMANCE ---")
    print(classification_report(y_true, y_pred, target_names=["Stress_faible", "Stress_fort", "Stress_moyen"]))
    
    acc = accuracy_score(y_true, y_pred)
    print(f"🏆 Précision globale (Accuracy) : {acc:.2%}")
    print("---------------------------------")

if __name__ == "__main__":
    evaluate_model()