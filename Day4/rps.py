import random

plr_input = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors."))

enemyInput = random.randint(0, 2)

print(f"0 means ROCK, 1 means PAPER and 2 means SCISSORS!")

print(f"Computer chose: {enemyInput}")

print(f"You played: {plr_input}")

if enemyInput == 0:
    if plr_input == 0:
        print("DRAW")
    elif plr_input == 1:
        print("You win!")
    else:
        print("You lose!")
elif enemyInput == 1:
    if plr_input == 0:
        print("You lose!")
    elif plr_input == 1:
        print("DRAW")
    else:
        print("You Win!")
elif enemyInput == 2:
    if plr_input == 0:
        print("You Win!")
    elif plr_input == 1:
        print("You Lose!")
    else:
        print("DRAW")