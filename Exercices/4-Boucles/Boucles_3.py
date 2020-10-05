"""
Problème:
    Trier le tableau de nombres entiers "t" en utilisant un tri par insertion

Données:
    Le tableau de nombres entiers "t"

Résultat attendu:
    Un message affichant le tableau "t" trié
"""

t = [6, 9, -2, 0, 19, -5, 34, 87, -32, 2, 8, 9]

# Votre solution

for i in range(1, len(t)):
    cle = t[i]
    j = i
    while j > 0 and t[j-1] > cle:
        t[j] = t[j-1]
        j -= 1
    t[j] = cle

print(t)
