"""
Problème:
    En considérant un tableau de nombres réels, calculer la moyenne

Données:
    Un tableau t de nombres réels

Contrainte:
    Obligation d'utiliser une boucle

Résultat attendu:
    191.22222222222223
"""

t = [2, 4, 7, 9, 14, 78, 165, 567, 875]

# Votre solution

moyenne = 0
for el in t:
    moyenne += el
print(moyenne / len(t))