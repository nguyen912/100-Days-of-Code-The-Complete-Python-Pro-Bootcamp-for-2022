weight = input("Type your weight: ")
height = input("Type your height: ")
bmi = float(weight) / float(height) ** 2
round_bmi = round(bmi, 2)
format_bmi = "{:.2f}".format(round_bmi)
print(f"Your BMI is {format_bmi}")