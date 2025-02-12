# Écrire une fonction vérification_adn qui permet de renvoyer la valeur True si la chaîne
# d’ADN est valide, False si elle est invalide ('a', 't', 'c', 'g'.)
def verification_adn(chaine: str):
    # print(f"ma chaine tester est : {chaine}")
    for lettre in chaine:
        # print(f"je verifie la lettre {lettre}")
        if lettre not in 'atcg':
            # print(f"oups celle la convient pas ...")
            return False
    # print("tous est bon !!!")
    return True



# print(verification_adn("atcgz")) # false
# print(verification_adn("gcta")) # true

# 2. Écrire une fonction saisie_adn qui récupère une saisie, vérifie sa validité et renvoie une
# chaîne d’ADN valide sous forme de chaîne

# def saisie_adn(question):
#     ma_chaine = input(question)
#     if verification_adn(ma_chaine):
#         print("saisi valide ")
#         return ma_chaine
#     print("erreur de saisie !!!")


def saisie_adn(question):
    ma_chaine = input(question)
    while not verification_adn(ma_chaine):
        print("erreur de saisie !!!")
        ma_chaine = input(question)
    return ma_chaine


# saisie_adn("Veuillez saisir une chaine ADN (contient atcg) : ")
    
# 3. Écrire une fonction proportion qui reçoit deux paramètres une chaîne d’ADN et une
# séquence d’ADN Elle renverra le nombre d’occurrences de la séquence dans la chaîne

def proportion(chaine: str,sequence: str):
    return chaine.count(sequence)

# print(proportion("toto","to"))
# print(proportion("tata","e"))

# Bonus calcul du pourcentage

def pourcentage_sequence(chaine: str,sequence: str,proportion : int):
    return round(proportion * len(sequence) * 100 / len(chaine),2)




chaine_adn = saisie_adn("Veuillez saisir une chaine ADN (contient atcg) : ")
sequence_adn = saisie_adn("Veuillez saisir une sequence ADN  : ")

print(f"Il y a la sequence {sequence_adn} {proportion(chaine_adn,sequence_adn)} fois dans la chaine : {chaine_adn}")
print(f"Il y a la sequence {sequence_adn} {pourcentage_sequence(chaine_adn,sequence_adn,proportion(chaine_adn,sequence_adn))} % dans la chaine : {chaine_adn}")