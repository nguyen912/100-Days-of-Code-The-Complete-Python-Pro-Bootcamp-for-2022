import random
import options

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 3)
options.choose(your_choice)
print(f"Computer chose:")
options.choose(computer_choice)

if your_choice == computer_choice:
    print("Drawn!")
elif your_choice == 0 and computer_choice == 1:
    print("You lose!")
elif your_choice == 0 and computer_choice == 2:
    print("You won!")
elif your_choice == 1 and computer_choice == 0:
    print("You won!")
elif your_choice == 1 and computer_choice == 2:
    print("You lose!")
elif your_choice == 2 and computer_choice == 0:
    print("You lose!")
elif your_choice == 2 and computer_choice == 1:
    print("You won!")
