for var in range(0,10):
    print(var," je me repete !")

for element in ["un","deux","trois"]:
    print(element)

cpt = 0
while cpt < 5:
    print("mon compteur est a : ",cpt)
    cpt += 1

entry =None

while entry != "ok":
    entry = input("entrer ok :")
    if(entry == "stop"):
        break
    if(entry == "ok"):
        continue
    print("entrer la bonne valeur !")
