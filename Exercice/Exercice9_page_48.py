# nbr = int(input("Entrer une valeur entre 1 et 3 :"))

# while nbr < 1 or nbr > 3 :
#     print("valeur incorrect !")
#     nbr = int(input("Entrer une valeur entre 1 et 3 :"))

# while not(nbr>=1 and nbr<=3):
#     print("valeur incorrect !")
#     nbr = int(input("Entrer une valeur entre 1 et 3 :"))

while True :
    nbr = int(input("Entrer une valeur entre 1 et 3 :"))
    if(nbr>=1 and nbr<=3):
        print("bravo")
        break
    else : 
        print("valeur incorrect !")