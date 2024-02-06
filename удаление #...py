
n=input()
n  =int(n[1:])
lines = []

# Чтение n строк кода
for _ in range(n):
    line = input()
    line = line.split('#')[0]
    line = line.rstrip()  # Удаление символов пустого пространства в конце строки
    if line.startswith("#"):  # Проверка наличия символа решетки в начале строки
        continue  # Пропуск строки, так как это комментарий
    lines.append(line)  # Добавление строки в список

# Вывод строк кода без комментариев и символов пустого пространства в конце строки
for line in lines:
    print(line)