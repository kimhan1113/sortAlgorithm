

import math


def primenumber(x):

    for i in range(2, x):
        if x % i == 0:
            return False

    return True


primenumber(5)


def is_prime_number(x):

    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False

    return True