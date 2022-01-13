print("Welcome to the treasure island.\n"
      "\n"
      "¯\_(͡° ͜ʖ ͡°)_/¯\n"
      "\n"
      "Your mission here is to find the treasure. Good luck!!\n")

c_path = input("You're at a cross road. Where do you want to go? Type 'L' for Left or 'R' for Right\n")
if c_path != "l".lower():
      print("Sorry, you just die, pal. Game Over. :'( ")
else:
      lake = input("'You\'ve come to a lake. There is an island in the middle of the lake. Type 'W' to wait for a boat or 'S' to swim across it.\n")

if lake != "w".lower():
      print("Sorry, you just die, pal. Game Over. :'( ")
else:
      island = input("You arrived at the island unharmed. There's a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?.\n")

if island == "yellow".lower():
      print("Congratulations, you did it. YOU WIN!!")
else:
      print("Sorry, you just die, pal. Game Over. :'( ")

