print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? $")
percentage_tip = input("What percentage tip would you like to give? $")
number_of_people = input("How many people to split the bill? $")
avg_bill = int(total_bill) / int(number_of_people)
percentage_tip_as_float = int(percentage_tip) / 100
print(f"Each people should pay: ${avg_bill + avg_bill * percentage_tip_as_float}.")