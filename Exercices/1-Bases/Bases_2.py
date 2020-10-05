"""
Problème:
    Intervertir les valeurs de deux variables indépendantes (mettre la valeur de x dans y et inversemment).

Contraintes :
    Interdiction de définir manuellement les valeurs des variables (interdiction d'écrire des valeurs numériques).

Données :
    Variables x et y.
"""

x = 10
y = 20
print("Valeur de base de x: ", x)
print("Valeur de base de y: ", y)

# Votre solution

temp = x
x = y
y = temp

# ou
# x, y = y, x

print("Valeur actuelle de x: ", x)
print("Valeur actuelle de y: ", y)
