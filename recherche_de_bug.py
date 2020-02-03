import random

def random_attribut():
    print("Je suis l'ordinateur et je joue un nouveau coup")
    # random_IA = random.randint(0, 2)
    #
    # if random_IA == 0:
    #     random_IA = "pierre"
    # elif random_IA == 1:
    #     random_IA = "papier"
    # else:
    #     random_IA = "ciseaux"
    return "ciseaux"
player_choice = input("Taper pierre, papier, ciseaux ou (q)uitter: ")
print(random_attribut())
print("A")
if player_choice == random_attribut():
    print("egalité")
elif player_choice == "pierre" and random_attribut() == "papier":
    print("IA win")
elif player_choice == "pierre" and random_attribut() == "ciseaux":
    print("player win")
elif player_choice == "papier" and random_attribut() == "ciseaux":
    print("IA win")
elif player_choice == "papier" and random_attribut() == "pierre":
    print("Player win")
elif player_choice == "ciseaux" and random_attribut() == "pierre":
    print("IA win")
elif player_choice == "ciseaux" and random_attribut() == "papier":
    print("Player win")
elif player_choice == "q":
    pass
else:
    print("Entrée incorrecte")
print("B")


