alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction in ['encode', 'decode']:
        break
    else:
        print("Invalid direction! Please enter either 'encode' or 'decode'.")

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amt):
    cypher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = (position + shift_amt) % len(alphabet)
        cypher_text += alphabet[new_position]
    print(cypher_text)

def decrypt(hidden_text, shift_reduce):
    plain_txt = ""
    for letter in hidden_text:
        position = alphabet.index(letter)
        new_position = (position - shift_reduce) % len(alphabet)
        plain_txt += alphabet[new_position]
    print(plain_txt)

if direction == 'encode':
    encrypt(plain_text=text, shift_amt=shift)
elif direction == 'decode':
    decrypt(hidden_text=text, shift_reduce=shift)
