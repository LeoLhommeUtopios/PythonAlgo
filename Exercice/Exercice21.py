
mes_notes = []


print(len(mes_notes))

for i in range(1,16):
    nb = input(f"Saisir la note n°{i} : ")
    mes_notes.append(nb)

print(mes_notes)

for i in mes_notes:
    print(i)


print(len(mes_notes))