participants = ["Mario", "Luigi", "Link", "Peach", "Kirby"]

def panne_moteur(participants: list):
    premier = participants.pop(0)
    participants.append(premier)
    return participants

def passe_en_tete(participants: list):
    #participants.insert(1, participants.pop(0))

    temp = participants[0]
    participants[0] = participants[1]
    participants[1] = temp
    return participants

def sauve_honneur(participants: list): 
    participants[-1], participants[-2] = participants[-2], participants[-1]
    return participants

def tir_blaster(participants: list):
    return participants.pop(0)

def retour_inattendu(participants: list, participant_touche):
    participants.append(participant_touche)
    return participants

def affichage_course(participants: list): 
    affichage = ""
    for participant in participants:
        index = participants.index(participant)
        if index == 0:
            affichage = affichage + f"1er - {participant}, "
        else:
            affichage += f"{index+1}eme - {participant}, "

    print(affichage)

def podium(participants: list): 
    print(f"""
        1er {participants[0]}
2eme {participants[1]}
                3eme {participants[2]}
          """)

affichage_course(panne_moteur(participants))
affichage_course(passe_en_tete(participants))
affichage_course(sauve_honneur(participants))
participant_blasterise = tir_blaster(participants)
affichage_course(participants)
affichage_course(retour_inattendu(participants, participant_blasterise))

podium(participants)
