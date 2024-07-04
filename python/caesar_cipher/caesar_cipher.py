option = input('What do you want to do?\nEncrypt\nDecrypt\nResponse: ')
data = input('Enter the text to encrypt: ')
key = int(input("Enter the key: "))

def encrypt_decrypt(text, key, action):
    result = ""
    for character in text:
        if character.isalpha():
            ascii_offset = 65 if character.isupper() else 97
            result += chr((ord(character) + key - ascii_offset) % 26 + ascii_offset) if action == "encrypt" else chr((ord(character) - key - ascii_offset) % 26 + ascii_offset)
        else:
            result += character
    return result

if option in ["encrypt", "decrypt"]:
    processed_text = encrypt_decrypt(data, key, option)
    print(f"{option.capitalize()}ed Text: {processed_text}")
else:
    print("Invalid action.")