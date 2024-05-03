alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabetLetters = len(alphabet)

# Function to encrypt the user input
def encrypt(user_input, key):
    cipher = ''
    for letter in user_input:
        letter = letter.lower()
        if letter != ' ':
            index = alphabet.find(letter)
            if index == -1:
                cipher += letter
            else:
                newIndex = index + key
                if newIndex >= alphabetLetters:
                    newIndex -= alphabetLetters
                cipher += alphabet[newIndex]
    return cipher

# Function to decrypt the user input
def decrypt(cipherText, key):
    plainText = ''
    for letter in cipherText:
        letter = letter.lower()
        if letter != ' ':
            index = alphabet.find(letter)
            if index == -1:
                plainText += letter
            else:
                newIndex = index - key
                if newIndex < 0:
                    newIndex += alphabetLetters
                plainText += alphabet[newIndex]
    return plainText

# What will display on the screen first
print()
print('Ceaser Cypher')
print()

print('Encrypt of Decrypt?')
userInput = input('encrypt/decrypt: ').lower()
print()

# What will display if the user wants to encrypt their text
if userInput == 'encrypt':
    print('Encryption Selected')
    print()
    key = int(input('Enter the key (1 through 26): '))
    text = input('Enter the message to encrypt: ')
    cipherText = encrypt(text, key)
    print(f'Ciphertext: {cipherText}')

# What will display if the user wants to decrypt their text
elif userInput == 'decrypt':
    print('Decryption Selected')
    print()
    key = int(input('Enter the key (1 through 26): '))
    text = input('Enter the message to decrypt: ')
    plainText = decrypt(text, key)
    print(f'Plaintext: {plainText}')