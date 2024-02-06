def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
# print(is_prime(17))


def get_next_prime(num):
    next_num = num + 1
    while not is_prime(next_num):
        next_num += 1
    return next_num

print(get_next_prime(14))