import pandas as pd
import os

# Création du dossier data s'il n'existe pas
os.makedirs("data", exist_ok=True)

# --- LISTE 1 : STRESS FORT (Colère, Panique, Urgence, Menace) ---
stress_fort_phrases = [
    # Français
    "C'est inadmissible, mon vol a 3 heures de retard !",
    "Je vais rater ma correspondance à cause de vous, faites quelque chose !",
    "Mes bagages sont perdus, c'est une catastrophe absolue.",
    "Personne ne me répond, c'est un scandale !",
    "Je veux un remboursement immédiat, c'est du vol.",
    "Aidez-moi, j'ai perdu mon passeport, je suis paniqué !",
    "Je vais porter plainte contre la compagnie, c'est honteux.",
    "Mon enfant est malade, il faut un médecin tout de suite !",
    "Vous avez annulé mon vol sans prévenir, je suis bloqué !",
    "C'est la pire expérience de ma vie, plus jamais la RAM.",
    "Je suis coincé sur le tarmac depuis 2 heures sans eau.",
    "Le personnel au sol a été très agressif avec moi.",
    "C'est urgent ! Je dois absolument partir ce soir.",
    "On m'a volé mon portefeuille en salle d'embarquement !",
    # Anglais
    "This is a nightmare, I need help right now!",
    "I will sue this airline for incompetence.",
    "Where is my luggage? I've been waiting for hours!",
    "I demand to speak to a manager immediately!",
    "This service is absolutely terrible, I am furious.",
    "I missed my flight because of your slow check-in process.",
    "I am panicking, I don't know where to go!",
    "Stop ignoring me, this is an emergency!",
    "My flight was cancelled and no one is helping me.",
    "I am stuck in a foreign country with no money.",
    # Arabe
    "أين حقائبي؟ لقد انتظرت طويلاً وهذا غير مقبول!",
    "أريد التحدث مع المسؤول فوراً، هذه فوضى.",
    "لقد ضاعت رحلتي بسببكم، سأفقد أعصابي!",
    "خدمة سيئة جداً، لن أسافر معكم مجدداً.",
    "ساعدوني، لقد فقدت جواز سفري وأنا خائف!",
    "أشعر بغضب شديد من هذه المعاملة السيئة.",
    "أريد استرجاع أموالي فوراً، هذا احتيال.",
    "أين الطائرة؟ لا أحد يجيبني، ساعدوني!",
    "هذه كارثة، كيف تلغون الرحلة دون إخبارنا؟"
]

# --- LISTE 2 : STRESS MOYEN (Inquiétude, Confusion, Questions logistiques) ---
stress_moyen_phrases = [
    # Français
    "Pouvez-vous me dire où se trouve la porte D4 ?",
    "Je suis un peu inquiet pour le timing de ma correspondance.",
    "Est-ce que le vol est à l'heure ? Je n'ai pas d'info.",
    "Je ne trouve pas mon billet électronique sur l'application.",
    "La file d'attente est vraiment longue, vais-je passer ?",
    "Combien de temps faut-il pour passer la sécurité ?",
    "Y a-t-il du retard prévu pour le vol AT123 ?",
    "Est-ce que mes valises suivent automatiquement à Casa ?",
    "Je n'arrive pas à me connecter au Wi-Fi de l'aéroport.",
    "Où sont les toilettes les plus proches s'il vous plaît ?",
    "Puis-je changer de siège ? Je suis séparé de ma famille.",
    "Mon application RAM bug, je ne peux pas m'enregistrer.",
    "Savez-vous si le repas végétarien est bien confirmé ?",
    "Il fait un peu froid dans la salle d'attente.",
    # Anglais
    "Is the flight on time? I have a tight connection.",
    "I can't find my boarding pass on my phone, can you help?",
    "How long is the queue for security check?",
    "Where is the nearest charging station for my phone?",
    "I'm a bit confused about the gate number, screens are off.",
    "Do I need to pick up my bags in Casablanca or do they transfer?",
    "Is there a lounge I can access with my economy ticket?",
    "My app is not loading properly, I am worried.",
    "Can I upgrade my seat? How much does it cost?",
    "I think I left my jacket on the plane.",
    # Arabe
    "كم من الوقت يستغرق المرور عبر الأمن؟",
    "هل الرحلة في موعدها؟ أنا قلق قليلاً.",
    "لا أجد التذكرة في هاتفي، ماذا أفعل؟",
    "أين بوابة الصعود للطائرة؟ اللوحات غير واضحة.",
    "هل هناك مكان لشحن الهاتف؟ بطاريتي تنفد.",
    "أنا قلق بشأن الحقائب، هل ستصل معي؟",
    "هل يوجد إنترنت مجاني هنا؟ أحتاج للتواصل.",
    "هل يمكنني تغيير المقعد؟",
    "التطبيق لا يعمل، هل يمكنني التسجيل هنا؟",
    "هل هناك تأخير في الرحلة؟"
]

# --- LISTE 3 : STRESS FAIBLE (Satisfaction, Calme, Politesse, Détente) ---
stress_faible_phrases = [
    # Français
    "Merci beaucoup pour votre aide précieuse.",
    "Tout s'est très bien passé, merci à l'équipe.",
    "J'ai hâte de partir, tout est prêt pour les vacances.",
    "Le salon VIP est très agréable et reposant.",
    "Le personnel est souriant et efficace, bravo.",
    "Superbe vol, atterrissage en douceur.",
    "L'application est très facile à utiliser, j'aime bien.",
    "J'aime beaucoup voyager avec la RAM, c'est confortable.",
    "Merci pour le surclassement, c'est une belle surprise !",
    "Le repas était délicieux, félicitations au chef.",
    "Je suis bien arrivé, merci pour ce voyage.",
    "Bonjour, je voudrais juste une couverture s'il vous plaît.",
    "La musique d'ambiance est relaxante.",
    # Anglais
    "Great service, thank you very much for your help.",
    "Everything went smoothly, great flight experience.",
    "I am very relaxed in the lounge, nice atmosphere.",
    "The cabin crew was amazing and very polite.",
    "Looking forward to my next trip with RAM.",
    "Smooth landing, thanks to the pilot.",
    "I really like the new app design, it works well.",
    "Can I have a glass of water? Thank you.",
    "Just landed safely, everything is good.",
    "Boarding was fast and organized today.",
    # Arabe
    "شكرا جزيلا على المساعدة، بارك الله فيكم.",
    "الرحلة كانت مريحة جدا والمضيفون لطفاء.",
    "خدمة ممتازة وطاقم رائع، شكراً.",
    "أحب الشاي المغربي الذي تقدمونه في الطائرة.",
    "كل شيء على ما يرام، شكرا لكم.",
    "وصلت بسلام، الحمد لله.",
    "المطار جميل ومنظم، أنا مرتاح.",
    "شكرا على الترقية لدرجة الأعمال.",
    "أنا سعيد جداً بهذه التجربة."
]

# --- FUSION ET CRÉATION DU DATASET ---

# On combine toutes les phrases
all_text = stress_fort_phrases + stress_moyen_phrases + stress_faible_phrases

# On crée les labels correspondants automatiquement
all_labels = (
    ["Stress_fort"] * len(stress_fort_phrases) +
    ["Stress_moyen"] * len(stress_moyen_phrases) +
    ["Stress_faible"] * len(stress_faible_phrases)
)

# Vérification de sécurité
assert len(all_text) == len(all_labels), "Erreur : Nombre de textes et de labels différent !"

# Création du DataFrame et sauvegarde
df = pd.DataFrame({"text": all_text, "stress_label": all_labels})
df.to_csv("data/passenger_stress_data.csv", index=False)

print(f"✅ Nouveau dataset généré avec succès !")
print(f"📊 Statistiques :")
print(f"   - Stress Fort   : {len(stress_fort_phrases)} phrases")
print(f"   - Stress Moyen  : {len(stress_moyen_phrases)} phrases")
print(f"   - Stress Faible : {len(stress_faible_phrases)} phrases")
print(f"   - TOTAL         : {len(df)} phrases")