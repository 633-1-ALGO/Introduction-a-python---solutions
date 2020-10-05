"""
Problème:
    Créer une fonction qui permet de savoir si une phrase est un palindrome ou non.
    La fonction prend une chaine de caractère en paramètre et retourne vrai si c'est le cas, faux sinon

Règles:
    Les espaces, les accents et les majuscules/minucles ne sont pas pris en compte pour savoir si un mot est un palindrome.
    Seul la lettre compte !

Données:
    Une chaine de caractère a qui est un palindrome
    Une chaine de caractère b qui n'est pas un palindrome
"""

a = "Ésope reste ici et se repose"
b = "Ceci n'est pas un palindrome"

# Votre solution
import unicodedata


def est_palindrome(phrase: str) -> bool:
    phrase = phrase.lower()
    phrase = "".join(phrase.split(" "))
    phrase = str(unicodedata.normalize("NFD", phrase).encode('ascii', 'ignore').decode("utf-8"))
    return phrase == phrase[::-1]


print(est_palindrome(b))
