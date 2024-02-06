def caesar_cipher(text, shift):
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            if char.isupper():
                index = (alphabet_upper.index(char) + shift) % len(alphabet_upper)
                encrypted_text += alphabet_upper[index]
            else:
                index = (alphabet_lower.index(char) + shift) % len(alphabet_lower)
                encrypted_text += alphabet_lower[index]
        else:
            encrypted_text += char
    return encrypted_text

text = "Hawnj pk swhg xabkna ukq nqj."
# shift =-5
# encrypted_text = caesar_cipher(text, shift)
# print(encrypted_text)
decrypted_words = []

for shift in range(-25, 0):
    decrypted_text = caesar_cipher(text, shift)
    decrypted_words.append(decrypted_text)

print(decrypted_words)
