"""
Problème:
    En considérant 2 tableaux, afficher les éléments du 2ème tableau qui ne sont pas présents dans le premier tableau

Containtes:
    Obligation d'utiliser des boucles

Résultat attend:
    Un message affichant "6 12"
"""

a = [1, 3, 5, 7, 9, 10, 11]
b = [1, 3, 5, 6, 7, 9, 10, 11, 12]

# Votre solution
resultat = []
for el in b:
    if el not in a:
        resultat.append(el)

print(*resultat)