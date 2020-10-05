"""
Problème:
    En considérant 3 appartements totalement identiques, calculer les impôts à payer.
    L'impôt d'un appartement équivaut à 24% du prix de l'appartement.

Données:
    Le prix d'un appartement (tous les appartements sont identiques et coutent donc le même prix).

Résultat attendu:
    Afficher le message "Avec X appartement coutant XXX CHF, il faut payer XXX CHF d'impôts".
"""

prix = 134000

# Votre solution
nb = 3
taux = 24
impot = (prix * nb) / 100 * taux
print("Avec", nb, "appartement coutant", prix, ", il faut payer", impot, "CHF d'impôts.")