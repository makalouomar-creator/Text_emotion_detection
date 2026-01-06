import pandas as pd
import os

def merge_datasets():
    file1 = "data/passenger_stress_data.csv" # Le gros fichier (v1)
    file2 = "data/new_batch_data.csv"        # Le nouveau petit fichier (v2)
    output_file = "data/dataset_complet.csv" # Le résultat final

    # Vérification que les fichiers existent
    if not os.path.exists(file1) or not os.path.exists(file2):
        print("❌ Erreur : L'un des fichiers CSV source est introuvable.")
        print("   Assurez-vous d'avoir lancé 'create_dataset.py' ET 'create_more_data.py'.")
        return

    print("🔄 Chargement des fichiers...")
    df_1 = pd.read_csv(file1)
    df_2 = pd.read_csv(file2)

    print(f"   📄 Batch 1 : {len(df_1)} lignes")
    print(f"   📄 Batch 2 : {len(df_2)} lignes")

    # FUSION (Concaténation)
    # ignore_index=True est important pour recréer une numérotation propre (0, 1, 2... 116)
    df_final = pd.concat([df_1, df_2], ignore_index=True)

    # Sauvegarde
    df_final.to_csv(output_file, index=False)

    print("-" * 30)
    print(f"✅ Succès ! Fichier fusionné : '{output_file}'")
    print(f"📊 Taille Totale : {len(df_final)} phrases prêtes pour l'entraînement.")

if __name__ == "__main__":
    merge_datasets()