

number = int(input())
# Инициализируем переменные минимальной и максимальной цифр значениями первой цифры числа
min_digit = number % 10  # последняя цифра
max_digit = number % 10  # последняя цифра

number //= 10            # удаляем последнюю цифру

# Проходим по всем оставшимся цифрам и обновляем значения минимальной и максимальной цифр при необходимости
while number > 0:
    digit = number % 10  # последняя цифра
    if digit < min_digit:
        min_digit = digit
    if digit > max_digit:
        max_digit = digit
    number //= 10  # удаляем последнюю цифру

print('Максимальная цифра:', max_digit)
print('Минимальная цифра:', min_digit)






