from math import *


def solve(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        x1 = (-b + discriminant**0.5) / (2*a)
        x2 = (-b - discriminant**0.5) / (2*a)
        print(min(x1, x2))
        print(max(x1, x2))
    elif discriminant == 0:
        x = -b / (2*a)
        print(x)
    else:
        print('Нет корней')

a=float(input())
b=float(input())
c=float(input())
solve(a,b,c)





