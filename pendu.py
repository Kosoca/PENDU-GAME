import utils

secretWord = ""
infoWord = ""
nbTry = 6

utils.showMenu(nbTry)

option = utils.chooseOptions(input())

if(option == 1):
    secretWord = utils.enterSecretWord(option)
    infoWord = utils.enterInfoWord(option)
    utils.niveau1()
    utils.tryFindWord(input("Entrer un mot pour trouver le mot secret :\n"),
    secretWord,
    option,
    nbTry)
elif(option == 2):
    secretWord = utils.enterSecretWord(option)
    infoWord = utils.enterInfoWord(option)
    utils.niveau2()
    utils.tryFindWord(input("Entrer un mot pour trouver le mot secret :\n"),
    secretWord,
    option,
    nbTry)
else:
    print("Aucun niveau selectionné.")
