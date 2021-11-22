from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d code: {end_text}")


print(logo)

restart = True
while restart:
    direction = ""
    correct_format = False
    while not correct_format:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        if direction == "encode" or direction == "decode":
            correct_format = True
        else:
            print("Please type again!")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift %= 26

    caesar(text, shift, direction)

    ask_continue = input("Type 'yes' to try again. Otherwise, type 'no'.\n")
    if ask_continue == "no":
        restart = False
        print("Goodbye.")


