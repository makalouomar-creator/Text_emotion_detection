✈️ RAM – Module d'Analyse de Stress Passager (Canal Textuel)

Projet d'Innovation - Groupe 08 (École Centrale Casablanca)

Ce livrable représente la composante Text Emotion Detection intégrée au sein de l'assistant intelligent multimodal conçu pour Royal Air Maroc.

La vocation principale de ce module est d'assurer une analyse en temps réel des échanges textuels (via chatbot) afin d'identifier avec précision le niveau de stress des passagers. Cette détection permet de déclencher une intervention proactive et ciblée de la part des agents de support.

📋 Vue d'ensemble du Système

S'appuyant sur l'Intelligence Artificielle, le système classe les messages entrants selon trois degrés de criticité, indépendamment de la langue de communication.

Fonctionnalités Majeures

🌍 Traitement Multilingue Natif : Prise en charge intégrale du Français, de l'Anglais et de l'Arabe (incluant le traitement du Darija/Arabe dialectal sous forme écrite).

🧠 Compréhension Sémantique Avancée : Exploitation d'une architecture BERT pour saisir les nuances contextuelles au-delà de la simple détection de mots-clés.

🚨 Protocole d'Urgence : Identification et priorisation immédiate des cas classés "Stress Fort" (situations sanitaires, menaces de sécurité, états de panique).

🔄 Pipeline de Données Évolutif : Implémentation d'un mécanisme de fusion de données (Data Merging) permettant l'enrichissement continu de la base de connaissances.

📂 Architecture Technique du Projet

La structure du projet a été pensée de manière modulaire pour optimiser la maintenabilité du code et faciliter son intégration.

Text_emotion_detection/
├── data/
│   ├── passenger_stress_data.csv  # Lot 1 : Scénarios de base et classiques
│   ├── new_batch_data.csv         # Lot 2 : Cas limites (Edge cases) & techniques
│   └── dataset_complet.csv        # DATASET FINAL (Fusion des sources)
├── models/                        # (Répertoire dédié à la persistance du modèle fine-tuné)
├── notebooks/                     # Environnement de prototypage (Jupyter Notebooks)
├── src/
│   ├── config.py                  # Paramétrage global et templates de réponses
│   ├── text_preprocess.py         # Module de nettoyage et normalisation (NLP)
│   └── stress_inference.py        # Moteur principal d'inférence IA
├── create_dataset.py              # Script de génération de données (Batch 1)
├── create_more_data.py            # Script de génération avancée (Batch 2)
├── merge_data.py                  # Utilitaire de consolidation des datasets
├── evaluate_results.py            # Script de validation et calcul des métriques
├── streamlit_app.py               # Interface de Démonstration Interactive
└── requirements.txt               # Liste des dépendances logicielles Python


🛠️ Technologies et Modèles Employés

1. Le "Cerveau" : BERT (Bidirectional Encoder Representations from Transformers)

Notre solution repose sur le modèle nlptown/bert-base-multilingual-uncased-sentiment.

Pourquoi le choix de BERT ?
À la différence des architectures traditionnelles qui analysent le texte de manière linéaire (gauche vers droite), BERT possède la capacité de lire une phrase dans les deux sens simultanément.

Bidirectionnalité : Cette caractéristique est cruciale pour la désambiguïsation. Par exemple, le modèle distingue le sens du mot "volé" dans "J'ai volé vers Paris" (contexte de voyage aérien) par rapport à "On m'a volé mon sac" (contexte de délit), grâce à l'analyse des mots environnants.

Transfer Learning : Le modèle bénéficie d'un pré-entraînement sur un corpus de 104 langues, suivi d'une spécialisation (Fine-Tuning) pour l'analyse fine de sentiments.

2. Stack Technique (Socle Technologique)

Langage : Python 3.8+

Framework IA : PyTorch & Librairie Transformers (Hugging Face)

Data Processing : Pandas (Traitement et manipulation de DataFrames)

Interface Utilisateur : Streamlit

📊 Performance et Résultats d'Évaluation

La validation du modèle a été effectuée sur un jeu de données complet comprenant 121 situations distinctes, couvrant un spectre large (urgences médicales, incidents techniques, pertes de bagages, retours positifs).

Métriques Actuelles (Dataset v2)

Précision Globale (Accuracy) : 72.73%

Volume de test : 121 échantillons.

Classe de Stress

Précision (Precision)

Rappel (Recall)

Analyse Détaillée

🟢 Stress_faible

86%

95%

Performance excellente pour identifier les clients satisfaits ou neutres.

🔴 Stress_fort

57%

85%

Très bon rappel. Le système identifie correctement 85% des urgences réelles (Priorité Sécurité).

🟠 Stress_moyen

95%

42%

Le modèle adopte une sélectivité élevée concernant le stress modéré.

Note Stratégique : La configuration du système privilégie délibérément la maximisation du Rappel sur la classe Stress_fort. L'objectif est de garantir qu'aucune urgence vitale ne soit ignorée, acceptant en contrepartie un taux modéré de fausses alertes (Faux Positifs).

🚀 Guide d'Installation et d'Utilisation

1. Installation de l'environnement

Clonage du référentiel et installation des bibliothèques requises :

git clone [https://github.com/makalouomar-creator/Text_emotion_detection.git](https://github.com/makalouomar-creator/Text_emotion_detection.git)
cd Text_emotion_detection
pip install -r requirements.txt


2. Génération du Pipeline de Données

Le projet intègre un mécanisme de génération par lots (batches) pour simuler un processus d'apprentissage continu et incrémental.

# Étape 1 : Génération du jeu de données initial
python create_dataset.py

# Étape 2 : Génération des scénarios complexes additionnels (Batch 2)
python create_more_data.py

# Étape 3 : Fusion des sources vers le Dataset Maître
python merge_data.py


Cette action génère le fichier final data/dataset_complet.csv.

3. Lancer l'Évaluation

Pour exécuter les tests de performance sur les données consolidées :

python evaluate_results.py


4. Démarrer l'Interface de Démo

Pour interagir avec le chatbot en temps réel via l'interface graphique :

streamlit run streamlit_app.py


📦 Intégration Système (API Interne)

Le module assure la communication avec l'écosystème global via un format d'échange JSON standardisé :

{
  "modality": "text",
  "input_text": "Mon père fait un malaise cardiaque !",
  "raw_sentiment": "1 star",
  "stress_level": "Stress_fort",
  "confidence": 0.88,
  "recommendation": "URGENCE : Alerter immédiatement le personnel médical et rassurer le passager."
}


Développé avec ❤️ pour Royal Air Maroc