from src.stress_inference import get_stress_from_text
import json

if __name__ == "__main__":
    print("--- 🧪 Test de l'analyseur de stress textuel ---")
    
    # Quelques phrases pour tester différentes émotions et langues
    phrases_test = [
        "Je suis ravi de ce voyage, merci !",                # Positif -> Stress Faible
        "C'est inacceptable, je vais rater ma correspondance.", # Négatif -> Stress Fort
        "Quelle est la porte d'embarquement ?",              # Neutre/Question -> Stress Moyen
        "I am scared, where is my luggage?",                 # Anglais/Peur -> Stress Fort
        "شكرا جزيلا"                                         # Arabe/Positif -> Stress Faible
    ]
    
    for phrase in phrases_test:
        print(f"\n📝 Message: {phrase}")
        # Appel de la fonction d'inférence
        result = get_stress_from_text(phrase)
        
        # Affichage du JSON formatté
        print(f"📊 Résultat JSON: {json.dumps(result, indent=2, ensure_ascii=False)}")

    print("\n✅ Test terminé.")