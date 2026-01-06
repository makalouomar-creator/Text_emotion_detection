import pandas as pd
import os

# Création du dossier data s'il n'existe pas
os.makedirs("data", exist_ok=True)

data = {
    "text": [
        # --- Stress Fort (Colère, Peur, Urgence) ---
        "C'est inadmissible, mon vol a 3 heures de retard !",
        "I am going to miss my connection, this is a nightmare!",
        "أين حقائبي؟ لقد انتظرت أكثر من ساعة!", 
        "Personne ne me répond, je suis perdu dans l'aéroport.",
        "This service is terrible, I want a refund immediately.",
        "ساعدني، لقد فقدت جواز سفري!",
        "Je vais porter plainte contre la compagnie, c'est honteux.",
        "My child is sick, I need a doctor now!",
        "لقد ألغيت رحلتي دون سابق إنذار، هذا غير مقبول.",
        "Il n'y a personne au guichet, je vais rater mon avion !",
        "Where is the manager? I need to speak to someone in charge!",
        "لقد سرقت محفظتي في قاعة الانتظار!",
        "C'est la pire expérience de ma vie, plus jamais la RAM.",
        "I've been stuck on the tarmac for 2 hours with no water.",
        "أشعر بضيق في التنفس، ساعدوني.",

        # --- Stress Moyen (Inquiétude, Confusion, Logistique) ---
        "Pouvez-vous me dire où se trouve la porte D4 ?",
        "Is the flight on time? I'm a bit worried.",
        "كم من الوقت يستغرق المرور عبر الأمن؟",
        "Je ne trouve pas mon billet électronique sur l'application.",
        "The queue is very long, will I make it?",
        "هل هناك مكان لشحن هاتفي؟",
        "Est-ce que mes bagages suivent automatiquement à Casablanca ?",
        "How do I connect to the airport Wi-Fi?",
        "هل سيتم تقديم وجبة نباتية على متن الطائرة؟",
        "J'ai une correspondance courte de 40 minutes, c'est suffisant ?",
        "Can I upgrade my seat to business class?",
        "لا أجد الشاشة الخاصة برحلي.",
        "Où sont les toilettes les plus proches ?",
        "Is there a lounge access for economy passengers?",
        "كم سعر الوزن الزائد للحقيبة؟",

        # --- Stress Faible (Satisfaction, Calme, Politesse) ---
        "Merci beaucoup pour votre aide, c'est très clair.",
        "Great service, everything went smoothly.",
        "شكرا جزيلا، الرحلة كانت مريحة.",
        "J'ai hâte de décoller, tout est prêt.",
        "The lounge is very relaxing, thank you.",
        "أين يمكنني شراء القهوة؟",
        "Le personnel de bord était très aimable.",
        "Just landed in New York, smooth flight.",
        "أحب الشاي المغربي الذي تقدمونه.",
        "L'application est très pratique, merci.",
        "Can I have a blanket, please?",
        "كل شيء على ما يرام، شكراً.",
        "J'aime beaucoup la musique d'ambiance.",
        "Boarding was very fast today.",
        "الجو جميل في الدار البيضاء."
    ],
    "stress_label": [
        # On multiplie les labels pour correspondre aux 15 phrases par catégorie
        "Stress_fort" for _ in range(15)] + 
        ["Stress_moyen" for _ in range(15)] + 
        ["Stress_faible" for _ in range(15)]
}

# Vérification de sécurité pour être sûr que les listes ont la même taille
assert len(data["text"]) == len(data["stress_label"]), "Erreur: Les listes n'ont pas la même taille !"

df = pd.DataFrame(data)
df.to_csv("data/passenger_stress_data.csv", index=False)

print(f"✅ Fichier 'data/passenger_stress_data.csv' généré avec succès ({len(df)} lignes).")