import json

with open('morse_codes.json') as file:
    morse_code_file = json.load(file)

alphabet_list = list(morse_code_file.keys())
code_list = list(morse_code_file.values())


def encode(text):
    encoded_text = ''
    for char in text:
        if char == " ":
            encoded_text += '/ '
        elif char in alphabet_list:
            encoded_text += f'{code_list[alphabet_list.index(char)]} '

    return encoded_text.strip()


def decode(code):
    decoded_text = ''
    code_split = code.split(' ')
    for char in code_split:
        if char == '/':
            decoded_text += ' '
        elif char in code_list:
            decoded_text += alphabet_list[code_list.index(char)]
        else:
            return f"Invalid character involved {char} "
    return decoded_text.strip()


exit_loop = False

while not exit_loop:
    choice = input('Do you want to encode or decode(e/d)').lower()

    if choice == 'e':
        text_to_code = input('Enter the text to encode : ')
        print(encode(text_to_code.strip().lower()))
    elif choice == 'd':
        code_to_text = input('Enter the code to decode : ')
        print(decode(code_to_text.strip()))
    else:
        print("invalid request")

    if input("do you want to continue(y/n)").lower() != 'y':
        exit_loop = True




