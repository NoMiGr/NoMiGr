import string
import random

def generate_passwords(num_passwords, password_length, include_digits, include_uppercase, include_lowercase, include_symbols, exclude_symbols):
    symbols = ''
    if include_digits:
        symbols += string.digits
    if include_uppercase:
        symbols += string.ascii_uppercase
    if include_lowercase:
        symbols += string.ascii_lowercase
    if include_symbols:
        symbols += '!#$%&*+-=?@^_'

    for _ in range(num_passwords):
        password = ''.join(random.choice(symbols) for _ in range(password_length))
        if all(exclude_symbol not in password for exclude_symbol in exclude_symbols):
            print(password)

num_passwords = int(input('Введите количество паролей для генерации: '))
password_length = int(input('Введите длину одного пароля: '))
include_digits = input('Включать ли цифры (0123456789)? (y/n): ').lower() == 'y'
include_uppercase = input('Включать ли прописные буквы (ABCDEFGHIJKLMNOPQRSTUVWXYZ)? (y/n): ').lower() == 'y'
include_lowercase = input('Включать ли строчные буквы (abcdefghijklmnopqrstuvwxyz)? (y/n): ').lower() == 'y'
include_symbols = input('Включать ли символы (!#$%&*+-=?@^_)? (y/n): ').lower() == 'y'
exclude_symbols = 'il1Lo0O'
exclude_symbols_input = input('Исключить ли неоднозначные символы (il1Lo0O)? (y/n): ').lower() == 'y'
if exclude_symbols_input:
    exclude_symbols += 'il1Lo0O'

generate_passwords(num_passwords, password_length, include_digits, include_uppercase, include_lowercase, include_symbols, exclude_symbols)
