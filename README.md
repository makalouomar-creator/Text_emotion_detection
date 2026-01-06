Markdown

# ✈️ RAM - Détection de Stress Passager (Module Texte)

Ce projet est le module **Text Emotion Detection** de l'assistant intelligent développé pour **Royal Air Maroc (Groupe 08)**.

Il analyse les messages textuels des passagers (chatbot) pour détecter leur niveau de stress et proposer des actions recommandées aux agents.

## 📋 Fonctionnalités

* **Multilingue :** Supporte le Français, l'Anglais et l'Arabe.
* **Analyse de Sentiment :** Utilise un modèle BERT (`nlptown/bert-base-multilingual-uncased-sentiment`).
* **Classification du Stress :**
    * 🔴 **Stress_fort** (Colère, Peur, Urgence)
    * 🟠 **Stress_moyen** (Inquiétude, Confusion)
    * 🟢 **Stress_faible** (Satisfaction, Calme)
* **Recommandations Intelligentes :** Suggère une réponse empathique adaptée au niveau de stress.
* **Interface Démo :** Application Web interactive via Streamlit.

## 📂 Architecture du Projet

```text
Text_emotion_detection/
├── data/                  # Contient les jeux de données (CSV)
├── models/                # (Futur) Pour sauvegarder le modèle après fine-tuning
├── notebooks/             # Zone d'expérimentation (Jupyter Notebooks)
├── src/                   # Code source principal
│   ├── config.py          # Configuration (seuils, messages types)
│   ├── text_preprocess.py # Nettoyage du texte
│   └── stress_inference.py # Logique de prédiction IA
├── simple_test.py         # Test rapide en ligne de commande
├── evaluate_results.py    # Calcul de la précision sur le dataset
├── create_dataset.py      # Générateur de données synthétiques
├── streamlit_app.py       # Interface de démonstration
└── requirements.txt       # Liste des dépendances Python
🚀 Installation
Pré-requis : Python 3.8+ installé.

Installation des dépendances :

Bash

pip install -r requirements.txt
(Note : L'installation peut prendre quelques minutes lors du téléchargement de PyTorch).

🛠️ Utilisation
1. Générer les données
Avant de commencer, générez le fichier CSV d'entraînement contenant des phrases types (FR/EN/AR) :

Bash

python create_dataset.py
2. Test Rapide (Console)
Pour vérifier que le modèle fonctionne et voir le format JSON de sortie :

Bash

python simple_test.py
3. Évaluer la performance
Pour calculer la précision (Accuracy) du modèle sur l'ensemble du dataset :

Bash

python evaluate_results.py
4. Lancer la Démo Interactive (Chatbot)
Pour ouvrir l'interface visuelle et tester le système en temps réel :

Bash

streamlit run streamlit_app.py
📦 Format de Sortie (JSON)
Le module renvoie un objet standardisé pour faciliter l'intégration avec les modules Vocal et Facial :

JSON

{
  "modality": "text",
  "input_text": "C'est inadmissible, mon vol est annulé !",
  "raw_sentiment": "1 star",
  "stress_level": "Stress_fort",
  "confidence": 0.85,
  "recommendation": "Je suis sincèrement désolé..."
}
Projet Innovation - Groupe 08


Maintenant que ton module est documenté et opérationnel, quelle est la prochaine étape pour toi : souhaites-tu voir comment **partager ce code** avec ton groupe (via Git/GitHub) ou préfères-tu qu'on approfondisse le **fonctionnement du modèle BERT** que tu utilises ?