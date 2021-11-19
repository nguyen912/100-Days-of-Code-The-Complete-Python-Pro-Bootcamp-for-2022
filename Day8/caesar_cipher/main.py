alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

go_again = True


def execute_program(direction_input, text_input, shift_input):
    result = ""
    if direction_input == "encode":
        for letter in text_input:
            if letter in alphabet:
                result += alphabet[alphabet.index(letter) - shift_input]
            else:
                result += letter
        print("Here's the encoded result: " + result)
    elif direction_input == "decode":
        for letter in text_input:
            if letter in alphabet:
                shift_position = alphabet.index(letter) + shift_input
                if shift_position < len(alphabet):
                    result += alphabet[alphabet.index(letter) + shift_input]
                else:
                    final_shift_position = (len(alphabet) - shift_position) * -1
                    result += alphabet[final_shift_position]
            else:
                result += letter
        print("Here's the decoded result: " + result)
    go_again = input("Type 'yes' if you want to go again. Otherwise, type 'no'.")
    if go_again == 'yes':
        go_again = True
    elif go_again == 'no':
        go_again = False


while go_again:
    execute_program(direction, text, shift)
