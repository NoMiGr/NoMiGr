



#from fractions import Fraction
# n = int(input())  допишите программу, которая вычисляет и выводит рациональное число,
# равное значению выражения   1/1**2+1/2**2+1/3**2+1/4**2+и так далее до +1/n**2
# from fractions import Fraction
#
# def calculate_sum(n):
#     total_sum = 0
#     for i in range(1, n + 1):
#         total_sum += Fraction(1, i ** 2)
#     return total_sum
#
# def main():
#     n = int(input())
#     result = calculate_sum(n)
#     print(result)
#
# if __name__ == '__main__':
#     main()



# from fractions import Fraction    n = int(input())
# допишите программу, которая вычисляет и выводит рациональное число,
# равное значению выражения   1/1!+1/2!+1/3!+1/4!+и так далее до +1/n!
# from fractions import Fraction
# from math import factorial
#
# def calculate_sum(n):
#     total_sum = 0
#     for i in range(1, n + 1):
#         factorial_i = factorial(i)
#         total_sum += Fraction(1, factorial_i)
#     return total_sum
#
# def main():
#     n = int(input())
#     result = calculate_sum(n)
#     print(result)
#
# if __name__ == '__main__':
#     main()