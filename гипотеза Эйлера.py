
import math
def check_euler_hypothesis():
    for a in range(1, 30):
        print(a)
        for b in range(1, 90):
            for c in range(1, 115):
                for d in range(1, 135):
                    for e in range(1, 150):
                        sum_of_powers = math.pow(a, 5) + math.pow(b, 5) + math.pow(c, 5) + math.pow(d, 5)
                        if  math.pow(e, 5)==sum_of_powers:
                            return [a, b, c, d, int(e)]
    return None

result = check_euler_hypothesis()

if result:
    print("Четыре положительных целых числа, сумма 5-х степеней которых равна 5-й степени другого числа: ")
    print(f"a = {result[0]}, b = {result[1]}, c = {result[2]}, d = {result[3]}, e = {result[4]}")
else:
    print("Гипотеза Эйлера не опровергнута.")

# a = 27
# b = 84
# c = 110
# d = 133
# e = 144

