print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("You're at a crossroad, where do you want to go? Type 'left' or 'right'. ").lower()

if choice1 == "left":
    choice2 = input("You've come to a lake. There is an island in the middle of the lake. "
                    "Type 'wait' to wait for a boat. Type 'swim' to swim across. ").lower()

    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. "
                        "There is a house with 3 doors. One red, one yellow, and one blue. "
                        "Which colour do you choose? ").lower()

        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure. You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. They look hungry!")
            choice4 = input("Do you 'run' or 'tame' the beasts? ").lower()
            
            if choice4 == "run":
                print("You try to run, but the beasts are faster. Game Over.")
            elif choice4 == "tame":
                print("Surprisingly, the beasts become friendly and lead you to another secret room with treasure! You Win!")
            else:
                print("Your hesitation costs you. Game Over.")
        
        else:
            print("You chose a door that doesn't exist. Game Over.")

    elif choice2 == "swim":
        print("You got attacked by an angry trout. Game Over.")

    else:
        print("Confused, you hesitate and get lost. Game Over.")

elif choice1 == "right":
    print("You encounter a mysterious stranger who offers you a choice.")
    choice5 = input("Do you accept his 'help' or 'ignore' him? ").lower()
    
    if choice5 == "help":
        print("The stranger gives you a map! You follow it and find a hidden cave.")
        choice6 = input("Do you enter the 'cave' or keep walking 'forward'? ").lower()
        
        if choice6 == "cave":
            print("Inside the cave, you discover ancient writings that reveal the treasure's location. You Win!")
        elif choice6 == "forward":
            print("You walk into a swamp and get stuck. Game Over.")
        else:
            print("You hesitate and get lost. Game Over.")
    
    elif choice5 == "ignore":
        print("You walk ahead but fall into quicksand. Game Over.")

    else:
        print("Your indecision leads to your doom. Game Over.")

else:
    print("You fell into a hole. Game Over.")
