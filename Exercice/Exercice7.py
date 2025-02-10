age = int(input("Entrer un age : "))

if age < 3 :
    print("votre enfant n'as pas l'age de pratiquer")
elif age < 7 :
    print("la licence est 'baby'")
elif age < 9:
    print("la licence est 'poussin'")
elif age < 11 :
    print("la licence est 'pupille'")
elif age<13 :
    print("la licence est 'minime'")
else :
    print("la licence est 'cadet'")