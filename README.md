# Projet finance ESG

# Projet Finance ESG

Reproduction et amélioration de l'étude présentée dans le papier de référence 
*"K-means et analyse de clustering hiérarchique agglomératif des scores ESG, 
variations annuelles et rendements boursiers"*, appliquée à un nouvel univers 
d'investissement : 18 entreprises de la supply chain NVIDIA (données Bloomberg BESG, 2016-2026).

Le projet reprend la méthodologie initiale (K-means, CAH) puis propose des améliorations : 
standardisation par Z-score, réduction de dimension par ACP, et exploration d'algorithmes 
alternatifs (DBSCAN, GMM) pour une segmentation plus robuste des profils ESG.

## Structure du projet
```
├── data/ 
│   ├── Données brutes Bloomberg
│   └── clean/                # Données traitées par notebook
│       ├── notebook1/
│       ├── notebook2/
│       └── ...
├── notebooks/
│   ├── 01_nettoyage_exploration.ipynb
│   ├── 02_clustering.ipynb
│   ├── 03_ameliorations.ipynb
│   ├── 04_generation_rendements_yahoo.ipynb
│   ├── 05_analyse_esg_rendements_clustering.ipynb
│   └── figures/
├── papier_référence/         # Article de référence
└── pyproject.toml
```


## Prérequis

- Python 3.12+

## Installation

### 1. Installer uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Puis relancer le terminal ou exécuter :

```bash
source ~/.bashrc   # Linux
source ~/.zshrc    # macOS
```

### 2. Installer les dépendances

```bash
uv sync
```

### 3. Lancer les notebooks 


