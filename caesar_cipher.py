"""
Send secret messages to your friends (or enemies) with this caesar
cipher translator! This translator can encode and decode messages using
Caesar cipher of customisable shift.

(created from Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp Course)
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        lowercase_char = char.lower()
        if lowercase_char in alphabet:
            position = alphabet.index(lowercase_char)
            new_position = position + shift_amount
            if new_position >= 26:
                new_position = new_position % 26
            if char.isupper():
                end_text += alphabet[new_position].upper()
            else:
                end_text += alphabet[new_position]
        else:
            end_text += char

    print(f"Here's the {cipher_direction}d result: {end_text}")


running = True
while running:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    user_input = input("Type 'yes' if you wish to restart. Otherwise type 'no'.\n")
    if user_input == 'no':
        running = False
        print("Goodbye")
