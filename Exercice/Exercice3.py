from math import pi

hauteur = float(input("entrer la hauteur du cone droits : "))
rayon = float(input("entrer le rayon du cone droit : "))

volume = (hauteur*rayon**2*pi)/3

print(f"le volume de notre cone droit est de : {volume:0.3f} m3")