###############################################################
# Write a program that adds the digits in a 2 digit number.
# e.g. if the input was 35, then the output should be 3 + 5 = 8
###############################################################
two_digit_number = input("Type a two digit number: ")
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
result = first_digit + second_digit
print(f"The sum of 2 digits is {result}.")
