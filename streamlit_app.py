import streamlit as st
import json
import time
from src.stress_inference import get_stress_from_text

# Configuration de la page
st.set_page_config(page_title="RAM - Assistant Stress Passager", page_icon="✈️", layout="wide")

# En-tête avec logo (fictif) et titre
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Royal_Air_Maroc_logo.svg/320px-Royal_Air_Maroc_logo.svg.png", width=150)
st.title("✈️ Analyseur d'Émotions Passager (RAM)")
st.markdown("---")

# Zone principale : Simulation du Chat
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("💬 Simulation Chatbot")
    st.info("Entrez un message comme si vous étiez un passager à l'aéroport.")
    
    user_input = st.text_area("Message du passager :", height=150, placeholder="Ex: Je ne trouve pas mes bagages, c'est urgent !")
    
    analyze_btn = st.button("🔍 Analyser le Stress", use_container_width=True)

# Zone de résultats
with col2:
    st.subheader("🧠 Analyse IA")
    
    if analyze_btn and user_input:
        with st.spinner('Analyse du texte en cours...'):
            time.sleep(1) # Petit délai pour l'effet démo
            result = get_stress_from_text(user_input)
            
            stress = result['stress_level']
            conf = result['confidence']
            
            # Affichage dynamique selon le stress
            if stress == "Stress_fort":
                st.error(f"🚨 **Niveau : {stress}**")
                st.metric(label="Confiance", value=f"{conf:.1%}")
                st.write("👉 **Action recommandée :** Transfert immédiat à un agent humain.")
                
            elif stress == "Stress_moyen":
                st.warning(f"⚠️ **Niveau : {stress}**")
                st.metric(label="Confiance", value=f"{conf:.1%}")
                st.write("👉 **Action recommandée :** Proposer des informations rassurantes.")
                
            else:
                st.success(f"✅ **Niveau : {stress}**")
                st.metric(label="Confiance", value=f"{conf:.1%}")
                st.write("👉 **Action recommandée :** Continuer le dialogue standard.")

            st.markdown("---")
            st.caption("Sortie JSON brute (pour intégration) :")
            st.json(result)

    elif not user_input and analyze_btn:
        st.warning("Veuillez écrire un message d'abord.")
    
    else:
        st.write("En attente d'un message...")

# Pied de page
st.markdown("---")
st.markdown("**Projet Innovation - Groupe 08** | Module : *Text_emotion_detection*")