#
# a = int(input())
# b = int(input())
#
# def get_divisors_sum(n):
#     divisors_num = 0
#     divisors_sum = 0
#     for i in range(1, n+1):
#         if n % i == 0:
#             divisors_num += 1
#             divisors_sum += i
#     return divisors_num, divisors_sum
#
# def find_number_with_max_divisors_sum(a, b):
#     max_number = 0
#     max_sum = 0
#     num_del = 0
#     for num in range(a, b + 1):
#         divisors_num, divisors_sum = get_divisors_sum(num)
#         if divisors_sum > max_sum:
#             max_sum = divisors_sum
#             num_del = divisors_num
#             max_number = num
#         elif divisors_sum == max_sum and num > max_number:
#             max_sum = divisors_sum
#             num_del = divisors_num
#             max_number = num
#     return max_number, max_sum
#
# a1, b1 = find_number_with_max_divisors_sum(a, b)
# print(a1, b1)

def get_divisors_sum(n):
    divisors_num = 0
    for i in range(1, n+1):
        if n % i == 0:
            divisors_num += 1
    return divisors_num

n = int(input())

for num in range(1, n+1):
    a = get_divisors_sum(num)
    print(num,'+'* a,sep='')




