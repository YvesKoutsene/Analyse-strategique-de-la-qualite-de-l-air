# AQF - Air Quality France : Analyse Stratégique OpenData

> *« Transformer l'invisible (la pollution) en intelligence décisionnelle. »*

---

## Présentation du Projet
Ce projet est une immersion profonde dans les données de la **qualité de l'air en France**. L'objectif est de transformer des millions de mesures brutes multi-annuelles en une analyse stratégique claire, identifiant les tendances temporelles et les corrélations critiques entre les polluants et les facteurs environnementaux.

### Objectifs Stratégiques
1. **Pipeline ETL Robuste :** Nettoyage chirurgical des données hétérogènes (Python/Pandas).
2. **Intelligence Temporelle :** Détection des cycles saisonniers et des ruptures historiques (ex: impact du COVID-19).
3. **Indices de Criticité :** Création d'indicateurs personnalisés basés sur les seuils OMS.
4. **Visualisation Narrative :** Storytelling visuel pour transformer des chiffres complexes en graphiques actionnables.
5. **Recommandations Data-Driven :** Un rapport final synthétique pour guider les politiques publiques ou privées.

---

## Architecture du Projet
```text
AQF/
├── data/               # Le coffre-fort des données
│   ├── raw/            # Données brutes (Immuables)
│   └── processed/      # Données prêtes pour l'analyse
├── notebooks/          # Laboratoire d'expérimentation (Analyses exploratoires)
├── src/                # Code source modulaire (Scripts ETL et Analyses)
├── reports/            # Export des graphiques (figures/) et du rapport final
├── requirements.txt    # Liste des dépendances (Pandas, Matplotlib, Seaborn)
└── README.md           # La vitrine du projet
```

---

## Stack Technique
- **Langage :** Python 3.x
- **Manipulation de Données :** Pandas, Numpy
- **Visualisation :** Matplotlib, Seaborn, Plotly (interactif)
- **Outils :** Jupyter Notebook, Git, GitHub

---

## Statut du Projet
- [x] Définition de l'architecture logicielle.
- [x] Identification et acquisition du dataset optimal.
- [~] Nettoyage et transformation des données (ETL).
- [ ] Analyse descriptive et corrélations.
- [ ] Visualisation et rédaction du rapport final.

---
*Réalisé avec la précision et l'exigence d'une élite Data Analyst.*
