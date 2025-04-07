import pyperclip
import random
import string

# Demande des options à l'utilisateur
majuscule = input("Voulez-vous des majuscules ? (O/N) : ").lower() == "o"
symbole = input("Voulez-vous des symboles ? (O/N) : ").lower() == "o"
chiffre = input("Voulez-vous des chiffres ? (O/N) : ").lower() == "o"
plusieur = input("Voulez-vous plusieurs mots de passe ? (O/N) : ").lower() == "o"
if plusieur:
    nb = int(input("Combien de mots de passe ? : "))

# Demande la longueur
longueur = int(input("Longueur du mot de passe ? : "))

# Création de la liste de caractères possibles
caracteres = ""

if majuscule:
    caracteres += string.ascii_letters  # Majuscules + minuscules
else:
    caracteres += string.ascii_lowercase

if symbole:
    caracteres += string.punctuation

if chiffre:
    caracteres += string.digits

if plusieur:
    # Vérifie si on a bien au moins un type
    if not caracteres:
        print("Vous devez sélectionner au moins une option !")
    else:
        # Génère les mots de passe
        for i in range(nb):
            motDePasse = ''.join(random.choice(caracteres) for _ in range(longueur))
            print(f"🔐 Mot de passe généré {i + 1} : {motDePasse}")
            pyperclip.copy(motDePasse)
            print("Le mot de passe a été copié dans le presse-papier.")
            # Écrit le mot de passe dans le fichier
            with open("mot_de_passe.txt", "a") as file:
                file.write(f"Mot de passe généré : {motDePasse}\n")
else:
    # Vérifie si on a bien au moins un type
    if not caracteres:
        print("Vous devez sélectionner au moins une option !")
    else:
        # Génère le mot de passe
        motDePasse = ''.join(random.choice(caracteres) for _ in range(longueur))
        print(f"🔐 Mot de passe généré : {motDePasse}")
        pyperclip.copy(motDePasse)
        print("Le mot de passe a été copié dans le presse-papier.")
        # Écrit le mot de passe dans le fichier
        with open("mot_de_passe.txt", "a") as file:
            file.write(f"Mot de passe généré : {motDePasse}\n")
