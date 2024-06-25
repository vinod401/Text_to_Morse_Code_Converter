import json

with open('morse_codes.json') as file:
    morse_code_file = json.load(file)


def encode(text):

    encoded_text = ''
    for letter in text:
        if letter == " ":
            encoded_text += '/'
        elif letter in morse_code_file:
            encoded_text += f"{morse_code_file[letter]} "

    return encoded_text.strip()

#
# def decode(code):
#     decoded_text = ''
#     for char in code:
#         if char == '/':
#             decoded_text += " "
#             else


input_text = input("Enter something to convert to morse code : ")

print(encode(input_text.lower().strip()))
