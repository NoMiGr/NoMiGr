

# Вот пример функции `read_csv`, которая считывает данные из CSV-файла и возвращает список словарей:
#
# ```python
import csv

def read_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(dict(row))
    return data


# Вы можете использовать эту функцию, передавая ей путь к файлу data.csv, и она вернет список словарей, где каждый словарь представляет одну строку из CSV-файла.
#
# Пример использования:
#
# ```python
file_path = 'data.csv'
data = read_csv(file_path)
for row in data:
    print(row)

