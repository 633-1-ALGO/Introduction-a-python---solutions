"""
Problème:
    Réaliser un programme qui intervertit les positions de chaque élément à la position impaire n d'un tableau t avec l'élément n+1

Exemple:
    Tableau de départ:  [0, 1, 2, 3, 4, 5]
    Tableau transformé: [1, 0, 3, 2, 5, 4]

"""

t = [0, 1, 2, 3, 4, 5]

# Votre solution

for i in range(0, len(t) - 1, 2):
    temp = t[i]
    t[i] = t[i + 1]
    t[i + 1] = temp

print(t)
