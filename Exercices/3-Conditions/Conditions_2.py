"""
Problème:
    En considérant 2 variables numéraires, afficher si leur produit est positif, négatif ou nul.
    Vous pouvez modifier les valeurs des variables pour tester votre code.

Données:
    Les deux variables numéraires.

Contrainte:
    Interdiction de calculer le produit des deux variables.

Résultat attendu:
    Un message affichant "Produit positif" ou "Produit négatif" ou "Produit nul".
"""

x = 10
y = 3

# Votre solution
if (x > 0 and y > 0) or (x < 0 and y < 0):
    print("Produit positif")
elif x < 0 or y < 0:
    print("Produit négatif")
else:
    print("Produit nul")
