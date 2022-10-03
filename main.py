import random

options = ["Rock", "Paper", "Scissors"]

player_choice = int(input("Choose an option. (1 = rock, 2 = paper, 3 = scissors)."))
# In range = 1 - 3
if 1 <= player_choice <= 3:
    player_choice = player_choice - 1
    pChoice = options[player_choice]
    # Becuase array starts from 0.
else:
    print("Not a valid option.")
    quit()

ai_choice = random.randint(0, 2)
cChoice = options[ai_choice]

print("Your choice: " + pChoice)
print("Computer choice: " + cChoice)


if player_choice == ai_choice:
    print("Its a tie")
elif (player_choice == 0 and ai_choice == 2) or (player_choice == 1 and ai_choice == 0) or (player_choice == 2 and ai_choice == 1):
    print("You win.")
else:
    print("You lose.")

quit()
