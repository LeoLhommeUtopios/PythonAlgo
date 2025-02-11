def nom_complet(prenom: str = "John", nom: str = "Doe")-> str:
    return prenom + " " + nom


def nom_complet_v2(prenom,nom):
    return prenom + " " + nom


#prenom1 = nom_complet("christophe","delory")
#prenom2 = nom_complet()

#print(prenom1)
#print(prenom2)

print(nom_complet("christophe","delory"))
print(nom_complet())
