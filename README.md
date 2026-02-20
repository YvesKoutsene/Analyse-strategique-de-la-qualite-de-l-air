# Analyse Stratégique de la Qualité de l'Air en France

## Contexte du projet

Ce projet personnel (2026) vise à analyser l'évolution de la qualité de l'air en France à partir de données publiques. L'objectif est de transformer des données brutes en **insights actionnables** sur les tendances de pollution atmosphérique et leurs variations géographiques et temporelles.

Dans un contexte de transition écologique et de sensibilité croissante aux enjeux environnementaux, cette analyse permet de :
- Comprendre les **tendances longues** de la qualité de l'air
- Identifier les **zones géographiques les plus exposées**
- Analyser les **corrélations entre différents polluants**
- Formuler des **recommandations** pour la surveillance et l'action publique

---

## Objectifs du projet

| Objectif | Description |
|----------|-------------|
| **Nettoyage des données** | Traiter un dataset OpenData multi-annuel (valeurs manquantes, outliers, normalisation) |
| **Analyse exploratoire** | Comprendre la distribution des polluants et leurs variations |
| **Création d'indicateurs** | Taux de dépassement, moyennes régionales, tendances temporelles |
| **Analyse saisonnière** | Identifier les périodes critiques et les variations cycliques |
| **Corrélations** | Étudier les relations entre différents polluants |
| **Visualisations** | Créer des graphiques pertinents et un dashboard complémentaire |
| **Recommandations** | Proposer des pistes d'action basées sur les données |

---

## Technologies utilisées

| Domaine | Technologies |
|---------|-------------|
| **Langage** | Python 3.9+ |
| **Manipulation de données** | Pandas, NumPy |
| **Visualisation** | Matplotlib, Seaborn |
| **Analyse statistique** | SciPy, Statsmodels |
| **Notebooks** | Jupyter |
| **Dashboard** | (Optionnel) Power BI / Streamlit |
| **Contrôle de version** | Git, GitHub |

---

## Source des données

### Jeu de données principal

**Source :** [data.gouv.fr](https://www.data.gouv.fr/fr/) - Plateforme ouverte des données publiques françaises

**Dataset utilisé :** "Données de surveillance de la qualité de l'air en France" (ou équivalent)
- Période : 2015-2025 (10 années de données)
- Fréquence : Mesures horaires / quotidiennes
- Couverture : Nationale (régions et départements)

**Polluants analysés :**
| Polluant | Description | Seuils réglementaires |
|----------|-------------|----------------------|
| PM10 | Particules fines (diamètre < 10µm) | 50 µg/m³ (journalier) |
| PM2.5 | Particules très fines (< 2.5µm) | 25 µg/m³ (annuel) |
| NO2 | Dioxyde d'azote | 200 µg/m³ (horaire) |
| O3 | Ozone | 180 µg/m³ (horaire) |
| SO2 | Dioxyde de soufre | 125 µg/m³ (journalier) |

---
