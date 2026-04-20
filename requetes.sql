 
 --Requete de base 
 
 /*SELECT * 
 FROM ventes;
*/



--Chiffre d'affaires total

/*SELECT SUM(prix * qte) AS chiffre_affaires_total
FROM ventes;
*/



--Ventes par produit 

/*SELECT produit, SUM(qte) AS quantite
FROM ventes
GROUP BY produit;
*/

--Ventes par region

SELECT region, SUM(qte) AS Quantite
FROM ventes
GROUP BY region;
