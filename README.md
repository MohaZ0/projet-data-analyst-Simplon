# Projet Positionnement - Data Analyst Simplon

Analyse des ventes d'une PME (Simplon - test de positionnement).

## Contexte
À partir d'un fichier `ventes.csv` (39 lignes, 3 produits, 2 régions), j'ai réalisé :
- 3 requêtes SQL (CA total, ventes par produit, ventes par région)
- 2 graphiques Python avec Plotly (camemberts)
- Une synthèse des résultats

## Contenu du repo
- `ventes.csv` - Jeu de données source
- `Ventes_par_produit.py` + `.html` - Camembert des quantités vendues par produit
- `CA_par_produit.py` + `.html` - Camembert du CA par produit
- `synthese.md` - Résultats SQL et conclusions
- `requirements.txt` - Dépendances Python

## Résultats clés
- **CA total : 44 825 €**
- **Produit leader : Produit A** (1750 unités, 17 500 €)
- **Région la plus forte : Sud** (1775 unités, 24 100 €)

Voir [synthese.md](synthese.md) pour le détail.

## Lancer les scripts
```bash
python Ventes_par_produit.py
python CA_par_produit.py
```

## Auteur
Mohamed Belhadef
