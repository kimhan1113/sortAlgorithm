import math


def check_prime(n):

    if n < 2:
        return False

    sqrt_num = int(math.sqrt(n)) + 1

    for i in range(2, sqrt_num):
        if n % i == 0:
            return False
    return True


def convert(n, k):

    num = ""

    while(n > 0):
        num += str(n % k)
        n //= k

    num = num[::-1]
    return num


def solution(n, k):
    n = convert(n, k)
    n = n.split("0")
    answer = 0

    for member in n:
        if member == "":
            continue
        if check_prime(int(member)):
            answer += 1

    return answer
