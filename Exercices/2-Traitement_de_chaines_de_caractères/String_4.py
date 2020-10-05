"""
Problème:
    Afficher le nombre d'occurences du mot "deux" présent dans la chaine de caractères puis remplacer les mots "deux" par "trois".

Données:
    La chaine de caratères

Résultat attendu:
    Le mot deux est présent 2 fois dans le texte
    Trois champignons poussent sur trois souches d'arbres.

Bonus:
    Inverser le sens de lecture de la phrase
"""

s = "deux champignons poussent sur deux souches d'arbres."

# Votre solution

print("Le mot deux est présent {} fois dans le texte".format(s.count("deux")))
print(s.replace("deux", "trois"))
print(s[::-1])

s2 = s.split(" ")
s2.reverse()
print(" ".join(s2))



