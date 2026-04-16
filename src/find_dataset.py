import requests
import json

def find_air_quality_2023():
    queries = ["qualité de l'air", "mesures horaires", "polluants atmosphériques"]
    all_found = []

    for query in queries:
        print(f"--- Recherche de '{query}' ---")
        url = f"https://www.data.gouv.fr/api/1/datasets/?q={query}&page_size=30"
        r = requests.get(url)
        if r.status_code != 200: continue

        datasets = r.json().get('data', [])
        for ds in datasets:
            org = ds.get('organization', {})
            org_name = org.get('name', '') if org else ''
            
            print(f"Exploration: {ds['title']} (Org: {org_name})")
            
            r_detail = requests.get(f"https://www.data.gouv.fr/api/1/datasets/{ds['id']}/")
            resources = r_detail.json().get('resources', [])
            
            for res in resources:
                title = res.get('title', '').lower()
                url_res = res.get('url', '')
                if '2023' in title and ('.csv' in url_res or '.zip' in url_res):
                    all_found.append((f"{ds['title']} - {res.get('title')}", url_res))

    if all_found:
        print("RESSOUCES 2023 TROUVÉES :")
        for name, url in all_found[:20]: 
            print(f"- {name} : {url}")
    else:
        print("Aucune ressource 2023 trouvée.")

if __name__ == "__main__":
    find_air_quality_2023()
