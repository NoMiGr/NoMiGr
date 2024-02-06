def caesar_cipher(text, shift):
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    encrypted_text = ''
    for char in text:
        if char.lower() in alphabet:
            index = alphabet.index(char.lower())
            if shift > 0:
                index = (index + shift) % len(alphabet)
            else:
                index = (index + shift + len(alphabet)) % len(alphabet)

            if char.islower():
                encrypted_text += alphabet[index]
            else:
                encrypted_text += alphabet[index].upper()
        else:
            encrypted_text += char
    return encrypted_text


text = "Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг."
shift = -7
encrypted_text = caesar_cipher(text, shift)
print(encrypted_text)