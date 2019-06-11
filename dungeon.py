# Dungeon Exploration

# Stretch Goals:
#   Finish flavor text for final room
#   Use while True on last 2 rooms for invalid options


print("Welcome to the dungeon") # This is room1
while True:
    choice = input("Options \n" 
        "1. Search Room \n"
        "2. Leave \n"
        "> ")
    if choice == "1":
        print("You find a silver spoon and a door leading to the next room.")
        choice2  = input("Options \n"
            "1. Pick up spoon \n"
            "2. Go to next room \n"
            "> ")
        if choice2 == "1":
            print("You put the spoon in your bag. \n"
                "Nothing else to do here. You go to the next room.")
            spoon = True
            break
        elif choice2 == "2":
            print("You go to the next room.")
            spoon = False
            break

    elif choice == "2":
        print("You gave up, get out.")
        exit()
    else:
        print("Please pick a valid option")
        continue

def room3():
    print("You enter the oppulent (for a goblin) throneroom of what appears to be a large and revolting Goblin King.")
    choice6 = input("Options \n"
        "1. Fight \n"
        "2. Escape \n"
        "> ")
    if choice6 == "1":
        print("Something happens") # Rewrite these lines of flavor text
        choice7 = input("Options \n"
            "1. Mundane option \n"
            "2. Non-mundane option \n"
            "> ")
        if choice7 == "1":
            print("Good End")
            exit
        elif choice7 == "2":
            print("Bad End")
            exit()
    elif choice6 == "2":
        print("As you turn to run away you are clobbered into the floor by the Goblin King. \n"
            "GAME OVER")
        exit()


def room2(spoon):
    print("You enter the room and you see two goblins")
    choice3 = input("Otions \n"
        "1. Fight \n"
        "2. Escape \n"
        "> ")
    if choice3 == "1":
        if spoon == True:
            print("The sentient spoon unleashes itself from your bag and annhilates the goblins in a blinding ray of light \n"
                "The Goblins are dead and you find a door leading to another room. What would you like to do now?")
            choice4 = input("Options \n"
                "1. Search \n"
                "2. Go to next room \n"
                "> ")
            print("The spoon flys back into your bag")
            if choice4 == "1":
                print("You search the goblins and the rest of the room and find nothing of value. \n"
                    "You go to the next room \n")
                room3()
            elif choice4 == "2":
                print("You go to the next room")
                room3()
            
        elif spoon == False:
            print("The goblins tear you limb from limb\n"
                "GAME OVER")
            exit()
    elif choice3 == "2":
        print("As you turn to run away you hear a grinding noise from the floor. \n"
            "You look down and see the blackness of a bottomless pit. \n"
            "GAME OVER")
        exit()

room2(spoon)
            
