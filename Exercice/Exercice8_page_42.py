age = int(input("Saisir l'age : "))
salaire = float(input("Saisir le salaire : "))
experience = int(input("Saisir les années d'experiences : "))

message = ""
convient = True

if(age < 30):
    message += "Vous n'avez pas l'age minimum pour le poste \n"
    convient = False
if(salaire > 40000):
    message +="Le salaire exigé est trop élevé\n"
    convient = False
if(experience <= 5 ):
    message +="Vous n'avez pas assez d'experience\n"
    convient = False

if(convient):
    message += "Votre profil convient"

print(message)