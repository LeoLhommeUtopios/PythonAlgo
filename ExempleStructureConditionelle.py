age = int(input("Entrer votre age : "))


if age >= 21 :
    print("Vous etes majeur au USA !")
elif age >= 18 :
    print("Vous etes majeu en europe mais pas au USA")
else :
    print("Vous etes mineur")


var = None

match var :
    case "bleu":
        print("couleur primaire bleu")
    case "rouge":
        print("couleur primaire rouge")
    case "jaune":
        print("couleur primaire jaune")
    case "noir" "blanc" "magenta" "rose" "gris":
        print("pas une couleur primaire")
    case _:
        print("pas une couleur")

if(var == "bleu"):
    pass
elif (var == "rouge"):
    pass
elif (var == "jaune"):
    pass
elif(var == "blanc" or var == "noir" or var == "magenta" or var == "rose" or var == "gris"):
    pass
else :
    pass