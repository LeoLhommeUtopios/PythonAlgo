def hello_world():
   # print("Hello World !!!")
   return "Hello World !!!"


# hello_world()

ma_variable = hello_world()

print(f"valeur de ma_varible {ma_variable}")

def dire_bonjour(nom: str,prenom):
   print(f"Bonjour {nom.capitalize()} {prenom}")


dire_bonjour('toto','tata')

dire_bonjour('tutu','titi')

def say_hello(name = 'Loick'):
   print(f"Hello {name}")

say_hello('toto')
say_hello()
say_hello()
say_hello()
say_hello()
say_hello('christophe')
   
def nombre():
   a = 2*5
   b = 3
   c = 4
   return a, b, c

# a = nombre()
# print(a)

lettre_a, lettre_b, lettre_c = nombre()
print(lettre_a)
print(lettre_c)

def affiche_oui_si_pair(nombre):
    if nombre % 2 == 0:
      print("oui")
    else:
      print("non")

nb = int(input('veuillez saisir un nombre : '))

affiche_oui_si_pair(nb)


def retourne_oui_si_pair(nombre):
    if nombre % 2 == 0:
      return "oui"
    else:
      return "non"
    
resultat = retourne_oui_si_pair(nb)

print(f"retourne_oui_si_pair : {resultat}")