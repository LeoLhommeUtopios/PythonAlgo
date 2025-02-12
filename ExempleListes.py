# initialisation d'un liste
ma_liste = []

print(ma_liste)


ma_liste2 = [1,2,3,"toto",True,["a",True,25]]

print(ma_liste2)

# Attention l'index de notre liste commence à 0
print(ma_liste2[0])
print(ma_liste2[3])
print(ma_liste2[-1])


print(ma_liste2[-1][1])
print(ma_liste2[5][-2])
print(ma_liste2[5][1])


# Modifier un élement
# syntaxe
# nom_de_ma_liste[index] = "nouvelle valeur"
ma_liste2[4] = "titi"
print(ma_liste2)

ma_liste3 = [5,3,4,1,2]
print(ma_liste3)
ma_liste3.sort()
print(ma_liste3)
ma_liste3.sort(reverse=True)
print(ma_liste3)

# ajout d'un element a la fin de la liste
print(ma_liste2)
ma_liste2.append(30)
print(ma_liste2)

# ajout d'un element à un index precis
ma_liste2.insert(2,"tutu")
print(ma_liste2)

# ajouter une liste a une autre
ma_liste2.extend(ma_liste3)
print(ma_liste2)
ma_liste2.extend(["tata","Loick"])
print(ma_liste2)



ma_liste2.append(["tata","Loick"])
print(ma_liste2)

# retirer un element de la liste
# avec element
ma_liste2.remove(2)
print(ma_liste2)


# avec index
ma_liste2.pop(4)
print(ma_liste2)

ma_liste2[4].pop(1)
print(ma_liste2)

# pour parcourir votre liste
for element in ma_liste2:
    print(element)

# verifaction d'un type
ma_variable = "42"
print(type(ma_variable))

print(type(ma_liste2[0]))

