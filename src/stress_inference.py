import torch
import numpy as np
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from src.config import MODEL_NAME, LABELS_MAPPING
from src.text_preprocess import clean_passenger_text

class TextStressAnalyzer:
    def __init__(self):
        print(f"🔄 Chargement du modèle {MODEL_NAME}...")
        # On charge le tokenizer et le modèle depuis Hugging Face
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        self.model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
        print("✅ Modèle chargé et prêt.")

    def predict(self, text):
        """
        Prend un texte brut, retourne le niveau de stress et la confiance.
        """
        # 1. Nettoyage
        clean_text = clean_passenger_text(text)
        
        if not clean_text:
            return {
                "modality": "text",
                "stress_level": "Inconnu",
                "confidence": 0.0
            }

        # 2. Tokenization (Transformation du texte en chiffres pour le modèle)
        inputs = self.tokenizer(
            clean_text, 
            return_tensors="pt", 
            truncation=True, 
            padding=True, 
            max_length=512
        )
        
        # 3. Prédiction (Inférence)
        with torch.no_grad():
            outputs = self.model(**inputs)
            # On transforme les scores bruts (logits) en probabilités (0 à 1)
            probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
        
        # 4. Récupération du résultat
        score_index = torch.argmax(probabilities).item()
        confidence = probabilities[0][score_index].item()
        
        # Le modèle renvoie des labels "1 star", "2 stars"... on les convertit
        raw_label = self.model.config.id2label[score_index]
        
        # 5. Mapping vers Stress (Règle Métier définie dans config.py)
        stress_level = LABELS_MAPPING.get(raw_label, "Stress_moyen")
        
        # Format standardisé pour l'intégration avec le vocal/facial
        result = {
            "modality": "text",
            "input_text": clean_text,
            "raw_sentiment": raw_label,   # Ex: "1 star"
            "stress_level": stress_level, # Ex: "Stress_fort"
            "confidence": round(confidence, 4)
        }
        
        return result

# --- Instanciation globale ---
# On crée l'analyseur ici pour qu'il soit chargé une seule fois au démarrage
analyzer = TextStressAnalyzer()

def get_stress_from_text(text):
    """Fonction helper facile à importer ailleurs"""
    return analyzer.predict(text)