import requests
import os

def download_file(url, filename):
    print(f"Tentative de téléchargement de {filename}...")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        r = requests.get(url, headers=headers, stream=True, timeout=30)
        if r.status_code == 200:
            with open(filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"✅ {filename} téléchargé avec succès.")
            return True
        else:
            print(f"❌ Erreur {r.status_code} sur le serveur.")
            return False
    except Exception as e:
        print(f"⚠️ Erreur de connexion : {e}")
        return False

def main():
    raw_dir = "data/raw"
    if not os.path.exists(raw_dir): os.makedirs(raw_dir)

    # Liens ArcGIS Airparif 2023 consolidés
    files_to_download = {
        "airparif_2023_no2.csv": "https://opendata.arcgis.com/datasets/airparif-asso::2023-no2.csv",
        "airparif_2023_pm10.csv": "https://opendata.arcgis.com/datasets/airparif-asso::2023-pm10.csv"
    }

    for name, url in files_to_download.items():
        success = download_file(url, os.path.join(raw_dir, name))
        if not success:
            print(f"--- Échec pour {name}. On passe à la suite. ---")

if __name__ == "__main__":
    main()
