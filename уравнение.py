
# from math import *

# a,b,c,d,e=1,2,3,4,5
# print("Сумма=", a+ b+ c+ d+ e)
for a in range(50,101):
    # print(a)
    for b in range(49, 101):
        print(a,b)
        for c in range(49, 101):
            for d in range(49, 101):
                for e in range(49, 101):
                     if a**5+b**5+c**5+d**5 == (e)**5:
                          print("Сумма=", a+ b+ c+ d+ e)
                          break




