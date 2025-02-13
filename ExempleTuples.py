mon_tuple = ("toto",2,3,4)

print(f"mon jolie tuple : {mon_tuple}")

# Acceder a un element
print(f"Premier element {mon_tuple[0]}")
print(f"Dernier element {mon_tuple[-1]}")

# unpacking
a, b, c, _ = mon_tuple
print(f"Déballage a = {a} b = {b} c = {c}  ")

def recuperer_nombre(nombre):
    return nombre,nombre * 2 # tuple packing => on utilise un tuple pour tous renvoyer

print(recuperer_nombre(3))

valeur1, valeur2 = recuperer_nombre(2)
print(f"valeur 1 : {valeur1} et valeur 2 : {valeur2}")