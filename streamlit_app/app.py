import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Analyse ESG & Finance — Supply Chain NVIDIA",
    page_icon="📊",
    layout="wide",
)

ASSETS = Path(__file__).parent / "assets"


def img(name):
    path = ASSETS / name
    if path.exists():
        st.image(str(path), use_container_width=True)


# ── Sidebar navigation ──────────────────────────────────────────────
pages = [
    "Accueil",
    "Exploration des données",
    "Corrélations ESG — Rendements",
    "Clustering K-means",
    "Méthodes avancées",
    "Robustesse & Validation",
    "Conclusion",
]
page = st.sidebar.radio("Navigation", pages)

# ── Accueil ──────────────────────────────────────────────────────────
if page == "Accueil":
    st.title("Analyse ESG & Rendements Boursiers")
    st.subheader("Clustering de la supply chain NVIDIA (2016–2026)")

    st.markdown("""
    **Reproduction et amélioration** de l'étude :
    *K-means et analyse de clustering hiérarchique agglomératif des scores ESG,
    variations annuelles et rendements boursiers* (Rusu, Boloș, Leordeanu, 2023)

    ---

    **Univers d'investissement** : 18 entreprises de la supply chain NVIDIA
    **Source des scores ESG** : Bloomberg BESG (2016–2026)
    **Rendements** : Yahoo Finance (prix ajustés mensuels)

    ---
    """)

    col1, col2, col3 = st.columns(3)
    col1.metric("Entreprises", "18")
    col2.metric("Observations", "2 175")
    col3.metric("Période", "2016 — 2026")

    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Variance PC1", "83.8 %")
    col2.metric("Silhouette (K-means)", "0.37")
    col3.metric("Silhouette (DBSCAN)", "0.67")
    col4.metric("β ESG → Rendement", "0.092 *")

    st.markdown("""
    ### Méthodologie

    | Étape | Description |
    |-------|-------------|
    | **Prétraitement** | Nettoyage Bloomberg, fusion ESG + rendements Yahoo Finance |
    | **Standardisation** | Z-score pour corriger les biais d'échelle |
    | **Clustering** | K-means, CAH, DBSCAN, GMM |
    | **Réduction de dimension** | ACP (99.2 % de variance en 2 composantes) |
    | **Validation** | Bootstrap, stabilité temporelle, concordance inter-méthodes |
    | **Régression** | Effet ESG → rendement avec contrôle des effets temporels |

    ---
    *Naviguez dans les pages via le menu latéral pour explorer les résultats.*
    """)


# ── Exploration ──────────────────────────────────────────────────────
elif page == "Exploration des données":
    st.title("Exploration des données")

    st.header("Valeurs manquantes")
    st.markdown("""
    - **Taux de rendements manquants** : 0.96 %
    - **Lignes affectées** : 21 / 2 196 (supprimées → 2 175 observations)
    - Valeurs manquantes principalement en début de série (*left-censoring* Bloomberg)
    """)
    img("nb06_fig00.png")

    st.header("Distributions")
    st.markdown("Histogrammes avec KDE des scores ESG et rendements :")
    img("nb06_fig01.png")

    st.header("Détection des outliers")
    st.markdown("""
    Outliers détectés (méthode IQR) :
    - Env_Score : **0** | Soc_Score : **0** | ESG_Score : **0** | Return : **75**
    """)
    img("nb06_fig02.png")

    st.header("Relations bivariées ESG — Rendements")
    img("nb06_fig03.png")

    st.header("Effet de la standardisation Z-score")
    st.markdown("""
    Sans standardisation, les rendements (variance élevée) domineraient les distances
    en clustering. Le Z-score ramène toutes les variables à moyenne 0 et écart-type 1.
    """)
    c1, c2 = st.columns(2)
    with c1:
        st.caption("AVANT standardisation")
        img("nb06_fig04.png")
    with c2:
        st.caption("APRÈS standardisation")
        img("nb06_fig05.png")


# ── Corrélations ─────────────────────────────────────────────────────
elif page == "Corrélations ESG — Rendements":
    st.title("Corrélations ESG — Rendements")

    st.header("Matrice de corrélation")
    st.markdown("""
    Corrélations faibles (0.07 – 0.21) mais positives entre scores ESG et rendements.
    Relation descriptive — ne capture ni les non-linéarités ni les effets sectoriels.
    """)
    img("nb06_fig06.png")

    st.header("Scatter ESG vs Rendement (avec tendance)")
    st.markdown("""
    Relation positive mais faible. Le score ESG n'explique qu'une faible part
    de la variabilité des rendements.
    """)
    img("nb06_fig07.png")

    st.header("Rendement moyen par quartile ESG")
    st.markdown("""
    Relation **monotone** : les entreprises du quartile supérieur (Q4, ESG élevé)
    ont un rendement moyen supérieur à celles du quartile inférieur (Q1).
    """)
    img("nb06_fig08.png")

    st.header("Évolution temporelle ESG vs Rendement")
    st.markdown("""
    Le score ESG moyen montre une tendance haussière quasi monotone.
    Les rendements sont volatils et ne suivent pas la même dynamique.
    """)
    img("nb06_fig09.png")


# ── Clustering K-means ───────────────────────────────────────────────
elif page == "Clustering K-means":
    st.title("Clustering K-means")

    st.header("Sélection du nombre de clusters")
    st.markdown("""
    - **Méthode du coude** : inflexion autour de k = 4
    - **Silhouette maximale** : k = 2 (score ≈ 0.37)
    """)
    img("nb06_fig10.png")

    st.header("Projection PCA des clusters (k = 2)")
    st.markdown("""
    Séparation principalement le long de PC1 (facteur ESG dominant).
    Structure quasi unidimensionnelle — le rendement est secondaire.
    """)
    img("nb06_fig11.png")

    st.header("Profil des clusters")
    st.markdown("""
    | | Env Score | Soc Score | ESG Score | Rendement |
    |---|---|---|---|---|
    | **Cluster 0** (ESG élevé) | 5.64 | 5.07 | 5.77 | **0.79** |
    | **Cluster 1** (ESG faible) | 3.36 | 2.24 | 3.55 | **0.29** |

    Le cluster à ESG élevé présente un rendement moyen **2.7× supérieur**.
    """)
    img("nb06_fig12.png")


# ── Méthodes avancées ────────────────────────────────────────────────
elif page == "Méthodes avancées":
    st.title("Méthodes avancées (Notebook 03)")

    st.header("Analyse en Composantes Principales (ACP)")
    st.markdown("""
    | Composante | Valeur propre | Variance expliquée | Cumulée |
    |---|---|---|---|
    | PC1 | 2.629 | 83.8 % | 83.8 % |
    | PC2 | 0.482 | 15.4 % | 99.2 % |
    | PC3 | 0.025 | 0.8 % | 100 % |
    """)

    c1, c2 = st.columns(2)
    with c1:
        st.caption("Scree plot")
        img("nb03_fig00.png")
    with c2:
        st.caption("Variance cumulée")
        img("nb03_fig01.png")

    st.subheader("Cercle des corrélations")
    img("nb03_fig02.png")

    st.subheader("Carte factorielle (ACP)")
    img("nb03_fig03.png")

    st.header("K-means sur ACP")
    st.markdown("K-means appliqué aux composantes principales → k = 6, silhouette = **0.642**")
    img("nb03_fig04.png")

    st.header("DBSCAN")
    st.markdown("""
    - **Configuration** : eps = 0.5, min_samples = 2
    - **Clusters** : 5 + 10 outliers
    - **Silhouette** : **0.671** (meilleure séparation)
    """)
    c1, c2 = st.columns(2)
    with c1:
        st.caption("k-distance graph")
        img("nb03_fig05.png")
    with c2:
        st.caption("Clusters DBSCAN")
        img("nb03_fig06.png")

    st.header("GMM (Gaussian Mixture Model)")
    st.markdown("""
    - **Meilleur modèle** : k = 7, covariance = full
    - **BIC** : 80.2 | **Silhouette** : 0.376
    """)
    c1, c2 = st.columns(2)
    with c1:
        st.caption("BIC / AIC par nombre de composantes")
        img("nb03_fig07.png")
    with c2:
        st.caption("Clusters GMM")
        img("nb03_fig08.png")

    st.header("CAH — Comparaison des distances")
    st.markdown("Dendrogrammes avec différentes métriques de distance :")
    c1, c2 = st.columns(2)
    with c1:
        img("nb03_fig09.png")
    with c2:
        img("nb03_fig10.png")

    st.header("Comparaison globale des méthodes")
    st.markdown("""
    | Méthode | k | Silhouette | Calinski-Harabasz | Davies-Bouldin |
    |---------|---|------------|-------------------|----------------|
    | K-means (original) | 9 | 0.426 | 34.5 | 0.594 |
    | CAH Ward | 9 | 0.426 | 34.5 | 0.594 |
    | K-means (ACP) | 6 | **0.642** | 147.9 | 0.345 |
    | GMM | 7 | 0.376 | 29.2 | 0.638 |
    | DBSCAN | 5 | **0.671** | 92.2 | **0.334** |
    """)
    img("nb03_fig14.png")


# ── Robustesse ───────────────────────────────────────────────────────
elif page == "Robustesse & Validation":
    st.title("Robustesse & Validation")

    st.header("Stabilité temporelle")
    st.markdown("""
    Évolution du score de silhouette sur 122 dates (2016–2026).
    Stabilité moyenne des clusters : **0.659** (range 0.60 – 0.76).
    """)
    img("nb03_fig11.png")

    st.subheader("Heatmap temporelle d'appartenance aux clusters")
    img("nb03_fig12.png")

    st.header("Validation par Bootstrap")
    st.markdown("""
    - **200 itérations** de bootstrap
    - Silhouette moyenne : **0.329 ± 0.048**
    - IC 95 % : [0.221, 0.401]
    """)
    img("nb03_fig13.png")

    st.header("Régressions ESG → Rendement")
    st.markdown("""
    | Modèle | β ESG | p-value | R² |
    |--------|-------|---------|-----|
    | Return ~ ESG | 0.092 | **0.011** | 0.024 |
    | Return ~ ESG + Env + Soc | -0.074 | 0.772 | 0.043 |
    | Return ~ ESG + effets temporels | 0.112 | **0.009** | 0.278 |

    - **Modèle 1** : effet positif significatif (p < 0.05)
    - **Modèle 2** : multicolinéarité entre piliers ESG → coefficients instables
    - **Modèle 3** : effet persistant après contrôle temporel (R² = 0.28)
    """)


# ── Conclusion ───────────────────────────────────────────────────────
elif page == "Conclusion":
    st.title("Conclusion")

    st.header("Résultats principaux")
    st.markdown("""
    1. **Association ESG–Rendement positive mais modérée** : corrélation faible (0.07–0.21),
       mais effet significatif en régression (β = 0.092, p = 0.011)

    2. **Clustering robuste** : K-means sur ACP (silhouette 0.642) et DBSCAN (0.671)
       offrent les meilleures séparations

    3. **Cluster ESG élevé = rendement 2.7× supérieur** (0.79 vs 0.29)

    4. **Effet persistant** après contrôle des effets temporels (β = 0.112, p = 0.009)

    5. **Stabilité modérée** des clusters dans le temps (0.659) et en bootstrap (IC 95 % : [0.221, 0.401])
    """)

    st.header("Limites")
    st.markdown("""
    - Échantillon restreint (18 entreprises)
    - Pas de contrôle pour les effets fixes entreprise ni les facteurs financiers classiques
       (taille, bêta, momentum)
    - Hypothèse d'indépendance potentiellement violée dans les tests panel
    - Sensibilité possible aux choix de période et de spécification
    """)

    st.header("Perspectives")
    st.markdown("""
    - Élargir le panel (plus d'entreprises, plus de secteurs)
    - Introduire des effets fixes entreprise et des facteurs de risque standards
    - Explorer des modèles non-linéaires (Random Forest, XGBoost)
    - Tester la causalité (Granger, variables instrumentales)
    """)

    st.markdown("---")
    st.caption("Projet réalisé dans le cadre du Master MOSEF — Victoria Viddal")
