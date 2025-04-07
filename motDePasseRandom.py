import random
import string

majuscule = bool(input("Voulez-vous des majuscules ? (O/N) : "))
if majuscule == "O" or majuscule == "o":
    majuscule = True
else:
    majuscule = False
symbole = bool(input("Voulez-vous des symboles ? (O/N) : "))
if symbole == "O" or symbole == "o":
    symbole = True
else:
    symbole = False
chiffre = bool(input("Voulez-vous des chiffres ? (O/N) : "))
if chiffre == "O" or chiffre == "o":
    chiffre = True
else:
    chiffre = False
longueur = int(input("Longueur du mot de passe ? : "))
if majuscule and symbole and chiffre:
    def motDePasseRandom(longueur):
        chro = [string.ascii_letters + string.digits + string.punctuation]
        motDePasse = ''.join(random.choice(chro) for i in range(longueur))
        return motDePasse
elif majuscule and symbole:
    def motDePasseRandom(longueur):
        chro = [string.ascii_letters + string.punctuation]
        motDePasse = ''.join(random.choice(chro) for i in range(longueur))
        return motDePasse
elif majuscule and chiffre:
    def motDePasseRandom(longueur):
        chro = [string.ascii_letters + string.digits]
        motDePasse = ''.join(random.choice(chro) for i in range(longueur))
        return motDePasse
elif symbole and chiffre:
    def motDePasseRandom(longueur):
        chro = [string.digits + string.punctuation]
        motDePasse = ''.join(random.choice(chro) for i in range(longueur))
        return motDePasse
elif majuscule:
    def motDePasseRandom(longueur):
        chro = [string.ascii_letters]
        motDePasse = ''.join(random.choice(chro) for i in range(longueur))
        return motDePasse
elif symbole:
    def motDePasseRandom(longueur):
        chro = [string.punctuation]
        motDePasse = ''.join(random.choice(chro) for i in range(longueur))
        return motDePasse
elif chiffre:
    def motDePasseRandom(longueur):
        chro = [string.digits]
        motDePasse = ''.join(random.choice(chro) for i in range(longueur))
        return motDePasse