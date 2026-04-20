# Synthèse des résultats

Analyse du fichier ventes.csv (39 lignes, 3 produits A/B/C, 2 régions Nord/Sud).

## Chiffre d'affaires total
Résultat : 44825

Requête utilisée :
```sql
SELECT SUM(prix * qte) AS chiffre_affaires_total
FROM ventes;
```

## Ventes par produit
- Produit A : 1750
- Produit B : 1055
- Produit C : 575

```sql
SELECT produit, SUM(qte) AS quantite
FROM ventes
GROUP BY produit;
```

## Ventes par région
- Nord : 1605
- Sud : 1775

```sql
SELECT region, SUM(qte) AS Quantite
FROM ventes
GROUP BY region;
```

## Ce que je retiens
Le produit A est celui qui se vend le plus en quantité et c'est aussi celui qui rapporte le plus de CA (17500 sur 44825). La région Sud vend un peu plus que le Nord.
