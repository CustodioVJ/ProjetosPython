import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print("Your choice was:\n", game_images[user_choice])
print("Computer's choice:\n")

if user_choice == 0:
    s = random.randint(0, 2)
    print(game_images[s])
    if s == 1:
        print("You lose!")
    elif s == 2:
        print("You win!")
    else:
        print("It's a draw!")
elif user_choice == 1:
    s = random.randint(0, 2)
    print(game_images[s])
    if s == 2:
        print("You lose!")
    elif s == 0:
        print("You win!")
    else:
        print("It's a draw!")
elif user_choice == 2:
    s = random.randint(0, 2)
    print(game_images[s])
    if s == 0:
        print("You lose!")
    elif s == 1:
        print("You win!")
    else:
        print("It's a draw!")

