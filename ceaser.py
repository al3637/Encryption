alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabetLetters = len(alphabet)

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

def dencrypt(ciphertext, key):
    plaintext = ''
    for letter in ciphertext:
        letter = letter.lower()
        if letter != ' ':
            index = alphabet.find(letter)
            if index == -1:
                plaintext += letter
            else:
                newIndex = index - key
                if newIndex < 0:
                    newIndex += alphabetLetters
                plaintext += alphabet[newIndex]
    return plaintext

print()
print('Ceaser Cypher')
print()

print('Encrypt of Decrypt?')
userInput = input('encrypt/decrypt: ').lower()
print()
if userInput == 'encrypt':
    print('Encryption Selected')
    print()
    key = int(input('Enter the key (1 through 26): '))
    text = input('Enter the message to encrypt: ')
    cipherText = encrypt(text, key)
    print(f'Ciphertext: {cipherText}')

elif userInput == 'decrypt':
    print('Decryption Selected')
    print()
    key = int(input('Enter the key (1 through 26): '))
    text = input('Enter the message to decrypt: ')
    plainText = encrypt(text, key)
    print(f'Plaintext: {plainText}')