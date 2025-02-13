def saisie_nombre_notes():
    nombre = int(input("Combien de notes voulez-vous ? "))
    liste_notes = []
    for i in range(0,nombre):
        note = float(input(f"Entrer la note n°{i+1} : "))
        liste_notes.append(note)

    return liste_notes

# test de saisie_nombre_notes()
# test_liste_notes = saisie_nombre_notes()
# print(test_liste_notes)

def saisie_notes_negatif_stop():
    liste_notes = []
    while True:
        note = float(input("Saisir une note : "))
        if note >=0 and note <=20:
            liste_notes.append(note)
        else:
            print("Note erreur, on arrete la saisie")
            break
    return liste_notes

# test de saisie_notes_negatif_stop()
# test_liste_notes = saisie_notes_negatif_stop()
# print(test_liste_notes)


def saisie_notes_menu():
    while True:
        print("Bienvenue")
        print("1- Pour entrer un nombre de note connu\n2- Pour continuer la saisie j'usqu'a une note negative ")
        choix = input("Votre choix : ")
        match choix:
            case "1":
                return saisie_nombre_notes()
            case "2":
                return saisie_notes_negatif_stop()
            case _:
                print("Choix invalide")


#print(saisie_notes_menu())



def menu_min_max_moy(listes_notes):
    while True:
        print("""Faites votre choix :
1- Afficher la note minimale
2- Afficher la note max
3- Afficher la moyenne
4- Quitter le programme
""")
        choix_menu = input("Votre choix : ")
        match choix_menu:
            case "1":
                print(min(listes_notes))
            case "2":
                print(max(listes_notes))
            case "3":
                print(sum(listes_notes)/len(listes_notes))
            case "4":
                exit()
            case _:
                print("Choix invalide")


                
liste_notes = saisie_notes_menu()
menu_min_max_moy(liste_notes)

