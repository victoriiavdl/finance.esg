# Données

Les données ESG utilisées dans ce projet proviennent du **terminal Bloomberg (BESG)** et ne sont pas redistribuables.

## Pour reproduire l'analyse

1. **Scores ESG Bloomberg** : exporter depuis le terminal Bloomberg les scores Environmental, Social et ESG global pour les 18 entreprises de la supply chain NVIDIA (2016–2026), au format CSV.

2. **Rendements boursiers** : générés automatiquement via `yfinance` dans le notebook `04_generation_rendements_yahoo.ipynb`.

## Structure attendue

```
data/
├── ENVIRONMENTAL_SCORE.csv    # Export Bloomberg
├── SOCIAL_SCORE.csv           # Export Bloomberg
├── esg score.csv              # Export Bloomberg
└── clean/                     # Généré par les notebooks
    ├── notebook1/
    ├── notebook2/
    ├── notebook3/
    ├── notebook4/
    └── notebook5/
```

## Entreprises de l'échantillon

NVIDIA, Broadcom, TSMC, Alphabet, SK Hynix, Lam Research, Advantest, Tower Semiconductor, Microsoft, Lumentum, AMD, Fabrinet, Snowflake, Micron, Tesla, SoftBank, CREDO Technology, Siemens Energy, Monolithic Power, Elite Material, Celestica, Meta, Amazon.
