import string, random

alphabet = string.ascii_lowercase
punctuation = string.punctuation

letters = {}
positions = {}

for i in range(len(alphabet)):
    letters[alphabet[i]] = i + 1
    positions[i + 1] = alphabet[i]

def random_symbol():
    return punctuation[random.randint(0, len(punctuation) - 1)]

def is_space(i, j):
    return i == "5" and j == "#"

def encrypt(message: str):
    encrypted_message = ""

    for i in range(len(message)):
        if not message[i].isspace():
            if message[i] in alphabet:
                pos = letters[message[i]]
                op = 27 - pos
                encrypted_message += random_symbol()  + random_symbol() + positions[op]
            else:
                encrypted_message += random_symbol() + random_symbol() + message[i]
        else:
            encrypted_message += "#5s"

    return encrypted_message

def decrypt(message: str):
    decrypted_message = ""

    for i in range(2, len(message), 3):
        if is_space(message[i - 1], message[i - 2]):
            decrypted_message += " "
        else:
            if message[i] in alphabet:
                pos = letters[message[i]]
                op = 27 - pos
                decrypted_message += positions[op]
            else:
                decrypted_message += message[i]

    return decrypted_message


message = "it works!!"

encrypted_message = encrypt(message)
print(encrypted_message)

decrypted_message = decrypt(encrypted_message)
print(decrypted_message)