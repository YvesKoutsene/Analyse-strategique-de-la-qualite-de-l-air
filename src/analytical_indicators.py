import pandas as pd
import numpy as np
import os

def calculate_strategic_indicators(input_path, output_path):
    print(f"--- Calcul des indicateurs analytiques : {input_path} ---")
    
    df = pd.read_csv(input_path)
    df['Date de début'] = pd.to_datetime(df['Date de début'])
    
    # Définition des seuils de référence (OMS / Réglementaire)
    # NO2 : 40 µg/m3 (Limite annuelle, mais utilisée ici comme repère de pic)
    # PM10 : 45 µg/m3 (Limite journalière OMS)
    # PM2.5 : 15 µg/m3 (Limite journalière OMS)
    thresholds = {
        'NO2': 40,
        'PM10': 45,
        'PM2.5': 15
    }
    
    # 1. Agrégation par Organisme et Polluant
    summary = df.groupby(['Organisme', 'Polluant']).agg(
        moyenne=('valeur', 'mean'),
        maximum=('valeur', 'max'),
        ecart_type=('valeur', 'std'),
        nb_mesures=('valeur', 'count')
    ).reset_index()
    
    # 2. Calcul du Taux de Dépassement
    def get_exceedance_rate(row):
        polluant = row['Polluant']
        threshold = thresholds.get(polluant, 100)
        subset = df[(df['Organisme'] == row['Organisme']) & (df['Polluant'] == polluant)]
        if len(subset) == 0: return 0
        over_threshold = (subset['valeur'] > threshold).sum()
        return (over_threshold / len(subset)) * 100

    print("⚡ Calcul des taux de dépassement (ceci peut prendre quelques secondes)...")
    summary['taux_depassement_pct'] = summary.apply(get_exceedance_rate, axis=1)
    
    # 3. Attribution d'un Score de Santé (A à E)
    def assign_score(row):
        rate = row['taux_depassement_pct']
        if rate == 0: return 'A (Excellent)'
        elif rate < 5: return 'B (Bon)'
        elif rate < 15: return 'C (Modéré)'
        elif rate < 30: return 'D (Médiocre)'
        else: return 'E (Critique)'
        
    summary['score_sante'] = summary.apply(assign_score, axis=1)
    
    # 4. Sauvegarde du tableau de bord
    if not os.path.exists(os.path.dirname(output_path)):
        os.makedirs(os.path.dirname(output_path))
        
    summary.to_csv(output_path, index=False)
    print(f"Tableau de bord stratégique généré : {output_path}")
    return summary

if __name__ == "__main__":
    INPUT = 'data/processed/air_quality_cleaned.csv'
    OUTPUT = 'reports/indicators_summary.csv'
    
    if os.path.exists(INPUT):
        calculate_strategic_indicators(INPUT, OUTPUT)
    else:
        print("Erreur : Fichier nettoyé introuvable.")
