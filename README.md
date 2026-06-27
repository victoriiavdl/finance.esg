# Analyse ESG & Rendements Boursiers — Supply Chain NVIDIA

Reproduction et amélioration de l'étude *"K-means et analyse de clustering hiérarchique agglomératif des scores ESG, variations annuelles et rendements boursiers"* (Rusu, Boloș, Leordeanu, 2023), appliquée à **18 entreprises de la supply chain NVIDIA** (données Bloomberg BESG, 2016–2026).

## Résultats clés

| Résultat | Valeur |
|----------|--------|
| Corrélation ESG–Rendement | 0.07 – 0.21 (positive, modérée) |
| Effet ESG en régression | β = 0.092, p = 0.011 |
| Avec contrôle temporel | β = 0.112, p = 0.009, R² = 0.28 |
| Rendement cluster ESG élevé | **0.79** vs 0.29 (×2.7) |
| Meilleure silhouette | DBSCAN : 0.671 |
| Variance ACP (2 composantes) | 99.2 % |

## Dashboard interactif

Les résultats sont présentés dans un **dashboard Streamlit** :

```bash
uv run streamlit run streamlit_app/app.py
```

## Structure du projet

```
├── data/                     # Données Bloomberg (non incluses, voir data/README.md)
├── notebooks/
│   ├── 01_nettoyage_exploration.ipynb
│   ├── 02_clustering_kmeans_cah.ipynb
│   ├── 03_ameliorations_avancees.ipynb
│   ├── 04_generation_rendements_yahoo.ipynb
│   ├── 05_analyse_esg_rendements_clustering.ipynb
│   └── 06_final.ipynb            # Notebook final de présentation
├── streamlit_app/
│   ├── app.py                    # Dashboard des résultats
│   └── assets/                   # Figures extraites des notebooks
├── papier_référence/             # Article de référence
└── pyproject.toml
```

> **Note** : Les données ESG proviennent du terminal Bloomberg (licence propriétaire) et ne sont pas distribuées. Voir [`data/README.md`](data/README.md) pour les instructions de reproduction.

## Méthodologie

1. **Prétraitement** : nettoyage des exports Bloomberg, fusion avec rendements Yahoo Finance
2. **Standardisation** : Z-score pour corriger les biais d'échelle
3. **Clustering** : K-means, CAH (Ward), DBSCAN, GMM
4. **Réduction de dimension** : ACP (83.8 % sur PC1, 99.2 % sur PC1–PC2)
5. **Validation** : bootstrap (200 itérations), stabilité temporelle, concordance inter-méthodes (ARI)
6. **Régression** : OLS avec erreurs robustes (HC3), effets temporels

## Installation

```bash
# Installer uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Installer les dépendances
uv sync
```

## Stack

Python 3.12+ · pandas · scikit-learn · matplotlib · seaborn · statsmodels · yfinance · Streamlit

## Contexte

Projet réalisé dans le cadre du **Master MOSEF** — Cours de Finance & ESG.
