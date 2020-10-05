"""
Problème:
    Écrire une suite de conditions permettant de trouver le prochain jour d'une date donnée

Exemple:
    Date donnée: 12.5.2020 -> Prochain jour: 13.5.2020
    Date donnée: 30.9.2020 -> Prochain jour: 1.10.2020

Règles:
    Afin de connaitre le prochain jour, il faut se baser sur certaines règles:

    Si le jour est plus petit que le nombre de jours dans le mois, on ajoute 1 au jour
    Sinon, il faut définir le jour à 1 et passer au prochain mois (attention de bien gérer le cas du nouvel an !)

    Pour connaitre le nombre de jours dans un mois:
        Si le mois est le numéro 1,3,5,7,8,10 ou 12, il a 31 jours
        Sinon si le mois est le numéro 2, il faut savoir si c'est une année bissextile.
            Si c'est le cas, il a 29 jours
            Sinon 28 jours.
        Sinon le mois à 30 jours

    Pour savoir si une année est bissextile:
        Si elle est un multiple de 400, c'est une année bissextile,
        Sinon si c'est un multiple de 100, ce n'est pas une année bissextile,
        Sinon si c'est un multiple de 4, c'est une année bissextile
        Sinon ce n'est pas une année bissextile

Données:
    Les variables représentant l'année, le mois et le jour.
    Vous pouvez modifier les valeurs de ces variables pour tester votre code

Résultat attendu:
    Un message affichant Le prochain jour de la date x.x.xxxx est x.x.xxxx.
"""

annee = 2020
mois = 9
jour = 30

# Votre solution
affichage = "Le prochain jour de la date {}.{}.{}".format(jour, mois, annee)

# Savoir si l'année est bissextile
est_bissextile = False
if annee % 400 == 0:
    est_bissextile = True
elif annee % 4 == 0:
    est_bissextile = True

# Connaitre le nombre de jours
nb_jours = 0
if mois in [1, 3, 5, 7, 8, 10, 12]:
    nb_jours = 31
elif mois == 2:
    if est_bissextile:
        nb_jours = 29
    else:
        nb_jours = 28
else:
    nb_jours = 30

# Trouver la prochaine date
if jour < nb_jours:
    jour = jour + 1
else:
    if mois == 12:
        jour = 1
        mois = 1
        annee = annee + 1
    else:
        jour = 1
        mois = mois + 1

print(affichage + " est {}.{}.{}.".format(jour, mois, annee))
