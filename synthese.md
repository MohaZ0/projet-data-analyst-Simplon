# Synthèse des analyses - Ventes PME

## Données
- 39 ventes enregistrées
- 3 produits : A, B, C
- 2 régions : Nord, Sud

## Résultats SQL

### 1. Chiffre d'affaires total
**44 825 €**

```sql
SELECT SUM(prix * qte) AS chiffre_affaires_total FROM ventes;
```

### 2. Ventes par produit (quantités)
| Produit   | Quantité |
|-----------|----------|
| Produit A | 1750     |
| Produit B | 1055     |
| Produit C | 575      |

```sql
SELECT produit, SUM(qte) FROM ventes GROUP BY produit;
```

### 3. Ventes par région (quantités)
| Région | Quantité |
|--------|----------|
| Nord   | 1605     |
| Sud    | 1775     |

```sql
SELECT region, SUM(qte) AS Quantite FROM ventes GROUP BY region;
```

## CA par produit (bonus)
| Produit   | CA (€) |
|-----------|--------|
| Produit A | 17 500 |
| Produit B | 15 825 |
| Produit C | 11 500 |

## Conclusions
- Le **Produit A** est le leader en volume (1750 unités) et en CA (17 500 €).
- La **région Sud** vend plus en quantité (1775) et en CA (24 100 €) que le Nord.
- Le CA total est réparti assez équilibré entre les 3 produits.
