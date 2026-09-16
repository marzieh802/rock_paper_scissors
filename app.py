# game
import sys
import random
your_input = input(
    "please enter a number \n 1 is stone \n 2 is paper \n 3 is scissor \n")


if not your_input.isdigit():
    print('is not digit ')
    sys.exit()
your_choice = int(your_input)

if your_choice >= 1 and your_choice <= 3:
    computer_choice = int(random.choice("123"))
    print(
        f"your choice is {your_choice} \ncomputer's choice is {computer_choice}")
    if your_choice == 1 and computer_choice == 3:
        print("u w")
    elif your_choice == 2 and computer_choice == 1:
        print("u w")
    elif your_choice == 3 and computer_choice == 2:
        print("u w")
    elif your_choice == computer_choice:
        print("tie")
    else:
        print("c w")

else:
    print("your number is out of range")
    sys.exit()
