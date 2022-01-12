print("Welcome to the tip calculator!!")

total = float(input("What was the total bill?\n"))
tip_percentage = int(input("What percetage would you like to give? 10, 12 or 15?\n"))
people = int(input("How many people to split the bill?\n"))

SS = (total + (total * tip_percentage/100)) / people

print("Each pearson should pay:", round(SS))