"""
Problème:
    Réalisez un programme qui permet de vérifier si un tableau est contenu dans un autre tableau.
    Vous pouvez modifier les valeurs des tableaux pour tester votre code

Données:
    Le tableau contenant a
    Le tableau contenu b

Contraintes:
    Obligation d'utiliser des boucles

Résultat:
    Un message affichant: "Le tableau b est contenu dans le tableau a" ou "Le tableau b n'est pas contenu dans le tableau a".
"""

a = [1, 2, 3, 4, 5]
b = [3, 4]

# Votre solution
contenu = False
for i in range(len(a) - len(b)):
    if a[i:i + len(b)] == b:
        contenu = True

if contenu:
    print("Le tableau {} est contenu dans le tableau {}".format(b, a))
else:
    print("Le tableau {} n'est pas contenu dans le tableau {}".format(b, a))
