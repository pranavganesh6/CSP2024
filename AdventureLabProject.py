import random

# Tell the user to choose a path between left or right
print("You are in a maze, you don't know why you are in it and only wish to survive.")
path = input("Choose between the path on the left or right (type 'left' or 'right'): ") == "right"

# If right, tell the users to choose between a man-eating plant, a vampire, or a lion that hasn't eaten in 6 weeks.
if path:
    i = int(input("Choose between option 1: a man-eating plant, option 2: a vampire, or option 3: a lion that hasn't eaten in 6 weeks. "))
    if i != 3:
        print("You DIED")
    else:
        print("The player wastes time thinking about if the lion is alive and becomes hungry.")

        spear = input("They come across a chest. Choose between a 'whole cooked chicken' or a 'spear': ") == "spear"

        # If chicken is chosen, hunger is restored. If spear is chosen, buff is given
        if spear:
            print("You are given an advantage.")
        else:
            print("Hunger is restored.")

        # Choose between acid, power plant, or swamp
        o = int(input("Choose between option 1: a vat of acid, option 2: an unstable electrical power plant, or option 3: a bacteria infested swamp: "))
        if o == 3:
            if random.random() <= 0.4 and not spear:
                print("The chicken gave food poisoning.")
                print("You DIED.")
            else:
                # Final choice: cheetah w/shark head or falcon w/wolf head
                d = int(input("Choose between option 1: fighting a cheetah with a shark's head or option 2: a falcon with a wolf's head. "))
                if d == 2 and spear:
                    print("You survived. You may now go to the final room.")
                    survive()
                elif d == 1:
                    print("You survived. You may now go to the final room.")
                    survive()
                else:
                    print("You DIED.")
        else:
            print("You DIED.")

else:
    # If left, choose between sharks or piranhas
    a = input("Choose between the left button: a tank full of sharks, or the right button: an ocean full of piranhas: ")
    if a == "right":
        print("The piranhas are all dead because they are freshwater fish.")
        print("You survived. You may now go to the final room.")
        survive()
    else:
        print("You DIED.")

# Main Room: Leads to the final decision
def survive():
    print("The kidnapper who trapped you here allows you to make 1 final decision: To take a 50/50 chance of dying or to die via decapitation.")
    print("He says that he has 2 pills: One harmless, one poisonous: You will take one pill and he will take the other. He says all the victims drank a glass of water with the pill. The victims died, but the kidnapper survived.")
    input("Choose between red and blue pill: ")
    water = input("Choose between water and no water: ") == "no water"
    decap = input("Decapitation? yes or no: ") == "yes"

    if not water or decap:
        print("DEAD")
    else:
        print("You sit for 20 mins and ESCAPE!")
