import pandas as pd
import os

def generate_new_batch():
    # Création du dossier si nécessaire
    os.makedirs("data", exist_ok=True)

    print("🛠️ Génération du nouveau lot de données (Batch 2)...")

    # --- LISTE DES PHRASES (Mélange FR / EN / AR) ---
    new_texts = [
        # === STRESS FORT (Urgences, Santé, Panique) ===
        "Mon mari fait un malaise, il me faut un médecin tout de suite !",
        "Il y a une odeur de brûlé en cabine, on a peur !",
        "There is a medical emergency at gate D4, please help!",
        "أشعر بضيق في التنفس، ساعدوني بسرعة!",
        "L'avion bouge trop, j'ai une crise de panique.",
        "On m'a volé mon passeport, je ne peux pas embarquer !",
        "This is totally unacceptable, I will call the police.",
        
        # === STRESS MOYEN (Problèmes App, Site, Confort) ===
        "L'application plante à chaque fois que je veux payer.",
        "Je n'arrive pas à choisir mon siège sur le site web.",
        "Le Wi-Fi ne marche pas, c'est embêtant pour mon travail.",
        "My vegetarian meal was not served, can you check?",
        "هل يمكنني استرجاع ثمن التذكرة؟",
        "Je ne trouve pas de prise électrique pour charger mon téléphone.",
        "Mon écran tactile est cassé au siège 14B.",
        "I didn't receive my booking confirmation email.",
        "La climatisation est trop forte, il fait froid.",

        # === STRESS FAIBLE (Compliments, Politesse) ===
        "Le personnel a été adorable avec mes enfants, merci.",
        "Super atterrissage, bravo au pilote.",
        "Thanks for the upgrade to Business Class!",
        "Les toilettes sont très propres, c'est appréciable.",
        "شكرا على الوجبة اللذيذة.",
        "L'embarquement était très rapide et organisé aujourd'hui."
    ]

    # --- LISTE DES LABELS CORRESPONDANTS ---
    new_labels = [
        # Fort (7 phrases)
        "Stress_fort", "Stress_fort", "Stress_fort", "Stress_fort", 
        "Stress_fort", "Stress_fort", "Stress_fort",

        # Moyen (9 phrases)
        "Stress_moyen", "Stress_moyen", "Stress_moyen", "Stress_moyen", 
        "Stress_moyen", "Stress_moyen", "Stress_moyen", "Stress_moyen", "Stress_moyen",

        # Faible (6 phrases)
        "Stress_faible", "Stress_faible", "Stress_faible", 
        "Stress_faible", "Stress_faible", "Stress_faible"
    ]

    # --- SÉCURITÉ : VÉRIFICATION DES TAILLES ---
    if len(new_texts) != len(new_labels):
        print(f"❌ ERREUR : Tu as {len(new_texts)} phrases mais {len(new_labels)} labels.")
        print("   -> Il faut avoir exactement le même nombre dans les deux listes !")
        return

    # --- CRÉATION DU CSV ---
    df = pd.DataFrame({
        "text": new_texts,
        "stress_label": new_labels
    })

    # Sauvegarde (avec encodage utf-8-sig pour bien gérer l'Arabe sur Excel/Windows)
    output_path = "data/new_batch_data.csv"
    df.to_csv(output_path, index=False, encoding='utf-8-sig')

    print(f"✅ Succès ! Fichier '{output_path}' créé.")
    print(f"📊 Contient {len(df)} nouvelles phrases prêtes à être fusionnées.")

if __name__ == "__main__":
    generate_new_batch()