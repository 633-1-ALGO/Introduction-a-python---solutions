"""
Problème:
    Créer une fonction prenant une chaine de caractère en paramètre et retournant
    le nombre de caractères en majuscules et le nombre de caractères en minuscule.

Données:
    La chaine de caractère s.

Résultat voulu:
    Un message affichant "La phrase "x" contient x caractères majuscules et x caractères minuscules".
"""

s = "Les pommes SONT très bonnes."


# Votre solution

def compteur_majuscules_minuscules(chaine: str) -> (int, int):
    nb_majuscules = 0
    nb_minuscules = 0
    for el in chaine:
        if el.isupper():
            nb_majuscules += 1
        else:
            nb_minuscules += 1
    return nb_majuscules, nb_minuscules


majuscules, minuscules = compteur_majuscules_minuscules(s)
print("La phrase \"{}\" contient {} caractères majuscules et {} caractères minuscules.".format(s, majuscules, minuscules))
