import random

numbers = [87, 0, 9, 2, 1, 8]
# for i in range(0, 6):
#     numbers.append(random.randint(0, 100))
# print(numbers)

odd_numbers = []
even_numbers = []
for i in numbers:
    if i == 0:
        print("This is 0.")
    elif i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)
print(even_numbers)
print(odd_numbers)
