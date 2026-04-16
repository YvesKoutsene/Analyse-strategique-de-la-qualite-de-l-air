# Air Quality France (AQF) : Ce que nous respirons vraiment

Bienvenue dans ce projet. Ici, on ne fait pas que manipuler des fichiers CSV. On a plongé dans les données réelles du **LCSQA** pour comprendre la réalité de la pollution de l'air en France en ce début d'année 2026. 

Pourquoi ce projet ? Parce que derrière chaque microgramme de poussière fine ou de dioxyde d'azote, il y a des enjeux de santé qui nous concernent tous : nos trajets pour aller bosser, le chauffage de nos maisons, et tout simplement la qualité de vie dans nos régions.

---

## Le constat : Entre ville et nature
J'ai analysé plus de **22 000 mesures** sur tout le territoire. Ce qui saute aux yeux, c'est ce contraste saisissant entre la pureté de l'air en Outre-mer et les défis énormes que rencontrent des régions comme l'Occitanie ou Auvergne-Rhône-Alpes en hiver.

### Ce que les chiffres nous racontent :

#### 1. Le rythme de nos journées
Le graphique ci-dessous montre bien que la pollution ne dort jamais vraiment, mais qu'elle a ses pics. On voit clairement l'impact de nos déplacements quotidiens sur les concentrations de NO2.
![Cycle Horaire](reports/figures/Cycle%20de%20Pollution%20Horaire%20Moyen%20(Janvier%202026).png)

#### 2. L'inégalité des régions
Toutes les régions ne sont pas logées à la même enseigne. Certaines dépassent les seuils recommandés par l'OMS de manière inquiétante. 
![Comparaison Régions](reports/figures/Concentration%20Moyenne%20de%20NO2%20par%20Organisme%20(Janvier%202026).png)

#### 3. La corrélation des polluants
On a aussi cherché à savoir si les polluants voyageaient ensemble. La réponse est oui : quand l'activité humaine s'intensifie, c'est tout le cocktail de polluants qui grimpe.
![Corrélation](reports/figures/Matrice%20de%20Corrélation%20entre%20les%20Polluants%20Stratégiques.png)

#### 4. Les jours critiques
Cette "carte de chaleur" nous montre les moments où l'air est devenu irrespirable dans certaines zones. C'est le miroir de notre activité et de la météo.
![Intensité Quotidienne](reports/figures/Intensité%20Quotidienne%20du%20NO2%20par%20Région%20(Janvier%202026).png)

---

## Comment j'ai bossé
J'ai voulu que ce projet soit aussi propre techniquement qu'un air de montagne :
- **Extraction & Nettoyage :** Un script Python qui trie le vrai du faux.
- **Analyse :** Utilisation de Pandas pour transformer la masse de données en indicateurs concrets.
- **Visualisation :** Des graphiques faits avec Seaborn pour que n'importe qui puisse comprendre en un coup d'œil.
- **Rapport :** Une synthèse stratégique avec de vraies recommandations (parce que la donnée doit servir à agir).

---

## Ma conclusion
La data science n'est utile que si elle aide à prendre de meilleures décisions. Ce projet m'a permis de mettre le doigt sur des zones rouges où l'action publique doit s'intensifier, notamment sur les particules fines en hiver.

*Si vous voulez en savoir plus, n'hésitez pas à jeter un œil au [Rapport Stratégique complet](reports/RAPPORT_STRATEGIQUE.md).*

---