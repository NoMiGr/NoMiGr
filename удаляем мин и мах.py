


# n = int(input())
#
# numbers = []
# for _ in range(n):
#     num = int(input())
#     numbers.append(num)
#     min_num = min(numbers)
#     max_num = max(numbers)
#     numbers.remove(min_num)
#     numbers.remove(max_num)
# for num in numbers:
#     print(num)


n = int(input())
numbers = []
for _ in range(n):
    number = int(input())
    numbers.append(number)

min_number = min(numbers)
max_number = max(numbers)

for number in numbers:
    if number != min_number and number != max_number:
        print(number)

