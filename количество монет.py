# from math import *
# количество пятёрок ,выход - или больше 5


price=int(input())

quarters = price // 25
price %= 25

dimes = price // 10
price %= 10

nickels = price // 5
price %= 5

pennies = price

total_coins = quarters + dimes + nickels + pennies

print(total_coins)




