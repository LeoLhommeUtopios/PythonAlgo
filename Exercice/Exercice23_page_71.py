def calcul(nb1,nb2):
    addition = nb1 + nb2
    soustraction = nb1 - nb2
    division = nb1 / nb2
    multiplication = nb1 * nb2
    return addition,soustraction,multiplication,division

nombre1 = float(input("Entrer le nombre 1 : "))
nombre2 = float(input("Entrer le nombre 2 : "))

#resultat1,resultat2,resultat3,resultat4 = calcul(nombre1, nombre2)
#print(f"La somme {resultat1}, le dividende est {resultat2}, le produit est {resultat3} et le quotient est {resultat4}.")

resultat = calcul(nombre1, nombre2)
print(resultat)
print(f"La somme {resultat[0]}, le dividende est {resultat[1]}, le produit est {resultat[2]} et le quotient est {round(resultat[3],2)}.")
