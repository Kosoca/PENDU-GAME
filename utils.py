def chooseOptions(result):
    if(result == "1"):
        return 1
    elif(result == "2"):
        return 2
    else:
        print("numéro incorrect, exit...")
        return 0

def enterSecretWord(result):
    if(result == 1):
        print("Demander à une personne tier d'entrer un mot secret...")
        return input("Entrer mot secret :\n")
    elif(result == 2):
        print("Demander à une personne tier d'entrer un mot secret...")
        return input("Entrer mot secret :\n")
    else:
        return ""

def enterInfoWord(result):
    if(result == 1):
        return input("Entrer une info sur le mot secret :\n")
    else:
        return ""


def tryFindWord(tryedWord, secretWord, lvl, nbTry):
    goodChar = 0
    indexChar = 0
    
    nbCharForWin = len(secretWord)

    for char in secretWord:
        if(tryedWord[indexChar] == char):
            goodChar += 1

        indexChar += 1
    if(goodChar == nbCharForWin):
        print(f"Vous avez gagné ! le mot est {tryedWord}")
    else:
        if(lvl == 1):
            print("lvl 1")
        elif(lvl == 2):
            print("lvl 2")


def showMenu(nbTry):
    print("#--------------------#")
    print("- Le pendu -")
    print("")
    print("Niveau 1 - facile (tapez [1])")
    print("Niveau 2 - normal (tapez [2])")
    print("")
    print(f"{nbTry} essaies sont disponible pour chaque partie.")
    print("")
    print("#--------------------#")
    print("Selectionner le niveau :")

def niveau1():
    print("#--------------------#")
    print("- Le pendu - Niveau 1")
    print("")
    print("- Une réponse avec l'emplacement des lettres bien placées.")
    print("- Le nombre de lettres bien placées.")
    print("- Une information complémentaire du mot choisi.")
    print("")
    print("#--------------------#")

def niveau2():
    print("#--------------------#")
    print("- Le pendu - Niveau 2")
    print("")
    print("- Uniquement le nombre de lettre bien placées.")
    print("")
    print("#--------------------#")

def showGallow(nbTry):
    if(nbTry == 6):
        print("#--------------------#")
        print("")
        print(" ________")
        print(" |      |")
        print(" |      O")
        print(" |      |")
        print(" |     _/\_")
        print(" |")
        print("_/\_")
        print("")
        print("#--------------------#")
    elif(nbTry == 5):
        print("#--------------------#")
        print("")
        print(" ________")
        print(" |      |")
        print(" |      O")
        print(" |")
        print(" |")
        print(" |")
        print("_/\_")
        print("")
        print("#--------------------#")
    elif(nbTry == 4):
        print("#--------------------#")
        print("")
        print(" ________")
        print(" |      |")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print("_/\_")
        print("")
        print("#--------------------#")
    elif(nbTry == 3):
        print("#--------------------#")
        print(" ________")
        print(" |      ")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print("_/\_")
        print("#--------------------#")
    elif(nbTry == 2):
        print("#--------------------#")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print("_/\_")
        print("#--------------------#")
    elif(nbTry == 1):
        print("#--------------------#")
        print("")
        print("_/\_")
        print("")
        print("#--------------------#")
    else:
        print("#--------------------#")
        print("")
        print("")
        print("")
        print("#--------------------#")
