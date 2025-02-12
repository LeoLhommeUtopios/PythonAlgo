# Écrire une fonction compter_lettre_a.
# Cette fonction prendra en paramètre une chaîne
def compter_lettre_a(chaine):
    cpt = 0
    print("je suis dans ma fonction compter_lettre_a")
    print(f"ma fonction a recu la chaine {chaine}")
    for i in chaine:
        print(i)
        if i == 'a':
            print("J'ai trouvé un a !!!!")
            cpt += 1 # cpt = cpt + 1
    print(f"mon compteur est à {cpt}")
    return cpt

# premier test
test1 = compter_lettre_a("toto")
test2 = compter_lettre_a("salut")
test3 = compter_lettre_a("baba")

print("#####################")
print()
print(test1)
print(test2)
print(test3)

test4 = compter_lettre_a("abba")
test5 = compter_lettre_a("mixer")

print("#####################")
print()
print(f"compter_lettre_a('abba') # résultat : {test4}")
print(f"compter_lettre_a('mixer') # résultat : {test5}")



def compter_lettre_a_avec_count(chaine: str):
    return chaine.count('a')

test6 = compter_lettre_a_avec_count("abba")
test7 = compter_lettre_a_avec_count("mixer")

print("#####################")
print()
print(f"compter_lettre_a_avec_count('abba') # résultat : {test6}")
print(f"compter_lettre_a_avec_count('mixer') # résultat : {test7}")