import pandas as pd
import os

def clean_air_quality_data(input_path, output_path):
    print(f"--- Démarrage du nettoyage : {input_path} ---")
    
    # 1. Chargement (sep=';' car c'est un CSV à la française)
    df = pd.read_csv(input_path, sep=';', low_memory=False)
    
    # 2. Sélection du "Trio Stratégique" de polluants
    target_pollutants = ['NO2', 'PM10', 'PM2.5']
    df_filtered = df[df['Polluant'].isin(target_pollutants)].copy()
    
    # 3. Typage et Nettoyage des dates
    # On transforme le texte en objet Datetime pour pouvoir faire des analyses par mois/heure
    df_filtered['Date de début'] = pd.to_datetime(df_filtered['Date de début'])
    
    # 4. Sélection des colonnes utiles (On élimine le surplus technique)
    useful_columns = [
        'Date de début', 'Organisme', 'nom site', 
        "type d'implantation", 'Polluant', 'valeur', 'unité de mesure'
    ]
    df_final = df_filtered[useful_columns].copy()
    
    # 5. Diagnostic rapide (Pour le rapport)
    missing_pct = df_final['valeur'].isnull().mean() * 100
    print(f"Filtrage terminé : {df_final.shape[0]} mesures conservées.")
    print(f"Taux de valeurs manquantes : {missing_pct:.2f}%")
    
    # 6. Sauvegarde du dataset "Propre"
    if not os.path.exists(os.path.dirname(output_path)):
        os.makedirs(os.path.dirname(output_path))
        
    df_final.to_csv(output_path, index=False)
    print(f"Dataset sauvegardé dans : {output_path}")
    return df_final

if __name__ == "__main__":
    RAW_FILE = 'data/raw/FR_E2_2026-01-01.csv'
    PROCESSED_FILE = 'data/processed/air_quality_cleaned.csv'
    
    if os.path.exists(RAW_FILE):
        clean_air_quality_data(RAW_FILE, PROCESSED_FILE)
    else:
        print("Erreur : Le fichier brut n'a pas été trouvé.")
