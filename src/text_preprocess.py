from cleantext import clean
import re

def clean_passenger_text(text):
    """
    Nettoie le message du passager avant analyse.
    Supporte le Français, l'Anglais et l'Arabe.
    """
    if not isinstance(text, str):
        return ""
    
    # Configuration de clean-text
    cleaned_text = clean(
        text,
        fix_unicode=True,               # Répare le texte mal encodé
        to_ascii=False,                 # TRÈS IMPORTANT : False pour garder l'Arabe et les accents !
        lower=True,                     # Tout en minuscule pour uniformiser
        no_urls=True,                   # Supprime les liens http://...
        no_emails=True,                 # Supprime les emails
        no_phone_numbers=True,          # Supprime les numéros de téléphone
        no_currency_symbols=False,      # On garde les symboles monétaires ($ €)
        no_punct=False,                 # On garde la ponctuation (! ?) car elle indique le stress
        no_emoji=False                  # On GARDE les emojis car ils sont cruciaux pour l'émotion
    )
    
    # Nettoyage final des espaces multiples
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    
    return cleaned_text

# Petit test si on lance ce fichier directement
if __name__ == "__main__":
    test_phrase = "HELP!!! Mon vol est annulé ??? 😡😡 http://ram.com"
    print(f"Original: {test_phrase}")
    print(f"Nettoyé : {clean_passenger_text(test_phrase)}")