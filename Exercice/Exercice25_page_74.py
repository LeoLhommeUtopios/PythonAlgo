def input_adress():
    address = {}
    address["N° de voie"] = input("Saisir N° de voie : ")
    address["Complément"] = input("Saisir Complément  : ")
    address["Intitulé"] = input("Saisir Intitulé : ")
    address["Commune"] = input("Saisir Commune : ")
    address["Code postal"] = input("Saisir Code postal: ")
    return address

def display_address(liste_adresses : list):
    print("=== Liste des Adresses ===")
    for adresse in liste_adresses:
        print(f"Adresse N° {liste_adresses.index(adresse)+1}")
        for key,value in adresse.items():
            print(f"  {key} : {value}")




def affiche_menu():
    print("=== Menu ===")
    print("1. Voir les adresses")
    print("2. Ajouter une adresse")
    print("3. Editer une adresse")
    print("4. Supprimmer une adresses")
    print("0. Quitter")


def handle_choice(liste_adresses : list):
    while True:
        affiche_menu()
        choice = input("Votre choix : ")
        while choice not in '12340':
            print("Erreur de choix.. \n")
            choice = input("Votre choix : ")
        match choice:
            case "1":
                if liste_adresses == []:
                    print("Pas encore d'adresse dans la liste !!!")
                else:
                    display_address(liste_adresses)
            case "2":
                liste_adresses.append(input_adress())
            case "3":
                display_address(liste_adresses)
                index = int(input("Numéro de l'adresse a modifier : ")) -1
                # liste_adresses.pop(index)
                # liste_adresses.append(input_adress())
                liste_adresses[index] = input_adress()
            case "4":
                display_address(liste_adresses)
                index = int(input("Numéro de l'adresse a suppr : ")) -1
                liste_adresses.pop(index)
            case "0":
                print("Aurevoir")
                break


list_adress = []
# list_adress.append(input_adress())
# list_adress.append(input_adress())

# display_address(list_adress)

handle_choice(list_adress)