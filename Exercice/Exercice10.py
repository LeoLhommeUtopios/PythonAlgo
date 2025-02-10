capital = float(input("Entrer votre capital : "))
taux = float(input("Entrer votre taux en % : "))/100
# capitalFinal = capital * 2
capitalIntial = capital
annee = 0

while capital < capitalIntial*2 :
    capital = capital * ( 1 + taux )
    annee = annee + 1


print(f" notre capital seras doublé au bout de {annee} années et seras de {capital}€")