mon_dict = {}

mon_dict = { 
    "Clé 1" : "Valeur 1",
    2 : 1,
    True : False
}

# Pour acceder a une valeur liee a une clé
print(f"valeur contenu a la Clé 1 : {mon_dict["Clé 1"]}")

# On re-affecte la valeur de la clé
mon_dict["Clé 1"] = "Toto"

print(f"valeur contenu a la Clé 1 : {mon_dict["Clé 1"]}")

# pour ajouter un élément :
print(mon_dict)
mon_dict["Clé 2"] = "casque"
print(mon_dict)

# supprime un élement
del mon_dict["Clé 2"]

print(mon_dict)


# attention une exception si la clé n'existe pas
# del mon_dict["Clé tuuututu"]

recup1 = mon_dict.pop(True)

print(mon_dict)
print(recup1)

# suprime et renvoie l'element(tuple)
recup = mon_dict.popitem()
print(mon_dict)
print(recup)

personne = {
    "prénom" : "christophe",
    "nom" : "toto",
    "age" : None
}

# fusion de dictionaire
print(personne)
personne.update(mon_dict)
print(personne)

# parcour de dictionnaire
for cle, valeur in personne.items():
    print(f"ma clé : {cle} et la valeur qui va avec {valeur}")



toto = {
    "prénom" : "toto",
    "nom" : "tata",
    "age" : 18
}

tata = {
    "prénom" : "tata",
    "nom" : "tutu",
    "age" : 81
}


titi = {
    "prénom" : "titi",
    "nom" : "haha",
    "age" : 56
}

annuaire = [toto,tata,titi]

print(annuaire)

for personne in annuaire:
    print(f"Personne n° {annuaire.index(personne)} qui s'apelle : {personne['prénom']}")
    for cle, valeur in personne.items():
        print(f"{cle} : {valeur}")

for i in annuaire:
    print(f"Personne n° {annuaire.index(i)}")
    for cle, valeur in i.items():
        print(f"{cle} : {valeur}")
