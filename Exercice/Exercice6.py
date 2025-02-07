nbcopie = int(input("Entrer le nombre de copies : "))

if nbcopie < 10 :
    prix = nbcopie * 0.5
elif nbcopie <= 20 :
    prix = nbcopie * 0.4
else :
    prix = nbcopie * 0.3

print(f"le total pour les {nbcopie} copies est de : {prix:0.2f} €")