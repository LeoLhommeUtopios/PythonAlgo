pop_init = int(input("Entrer la population initial : "))
taux = int(input("Entrer le taux en %"))/100
pop_final = int(input("Entrer la population final : "))
annee = 0

while pop_init < pop_final :
    pop_init = pop_init * (1+taux)
    annee += 1

print(f"la population attendras {pop_final} habitants au bout de {annee} années ")

