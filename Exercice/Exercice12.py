# max_value = None

# for i in range (1,7):
#     value = int(input(f"Entrer la valeur n° {i} : "))
#     if( max_value == None or max_value < value ):
#         max_value = value

max_value = int(input(f"Entrer la valeur n° 1 : "))

for i in range (2,7):
    value = int(input(f"Entrer la valeur n° {i} : "))
    if( max_value < value ):
        max_value = value


print("la valeur maximal est : ",max_value)