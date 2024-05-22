print("Welcome to treasure Island")
print("Your mission is to find the treasure")

user_input = input("You are at cross road. Where do you want to go? Type 'left' or 'right': ")

if user_input == "left":
    user_input = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait a boat to arrive, or 'swim' to swim across: ")
    if user_input == "wait":
        user_input = input("You arrive at the island unharmed. There are three doors, red, yellow and blue. Which colour do you choose? ")
        if user_input == "yellow":
            print("You Win!")
        elif user_input == "red":
            print("You burned by fire. \n Game Over!")
        elif user_input == "blue":
            print("Eaten by beasts. \n Game Over!")
        else:
            print("Game Over!")
    else:
        print("Attacked by trout. \n Game Over!")
else:
    print("You fall in the hole. \n Game Over!")