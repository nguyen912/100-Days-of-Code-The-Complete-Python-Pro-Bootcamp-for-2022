from art import logo


def add(number1, number2):
    return number1 + number2


def subtract(number1, number2):
    return number1 - number2


def multiply(number1, number2):
    return number1 * number2


def divide(number1, number2):
    return number1 / number2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculate():
    print(logo)
    calculate_finished = False
    first_number = float(input("What's the first number? "))
    for operation in operations:
        print(operation)

    should_continue = True
    while should_continue:
        operator = input("Pick an operation: ")
        next_number = float(input("What's the next number? "))

        chosen_operation = operations[operator]
        result = chosen_operation(first_number, next_number)

        print(f"{first_number} {operator} {next_number} = {result}")
        continue_calculating = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation.")
        if continue_calculating == "y":
            first_number = result
        elif continue_calculating == "n":
            calculate()
        else:
            return


calculate()
#
#
#
