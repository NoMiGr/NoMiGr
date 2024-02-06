


string = input()

# Создание списков гласных и согласных букв
vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
consonants = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']
# Инициализация счетчиков гласных и согласных букв
vowel_count = 0
consonant_count = 0
# Перебор символов строки
for char in string:
    if char.lower() in vowels:
        vowel_count += 1
    elif char.lower() in consonants:
        consonant_count += 1
# Вывод результата
print('Количество гласных букв равно', vowel_count)
print('Количество согласных букв равно', consonant_count)