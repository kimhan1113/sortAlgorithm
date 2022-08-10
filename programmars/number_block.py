from copy import deepcopy
import math


def is_prime_number(x):

    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False

    return True


def solution(begin, end):

    blocks = [0 for _ in range(end+1)]

    blocks[end] = int(end//2)
    finished = deepcopy(end)
    finished -= 1

    while(finished > 1):
        if is_prime_number(finished):

            blocks[finished] = 1

        elif finished % 2 == 0:
            blocks[finished] = finished // 2

        else:
            blocks[finished] = int(math.sqrt(finished))

        finished -= 1

    answer = blocks[begin:end+1]
    return answer


num = 8

print(math.sqrt(num))
print(num**0.5)


answer = solution(1, 10)


def solution(begin, end):
    answer = []
    for i in range(begin, end+1):
        k = int(i != 1)  # i가 1이면 0, 1이 아니면 1을 대입
        for j in range(2, int(i**0.5)+1):  # i**0.5 == sqrt(i)
            if i % j == 0 and i//j <= 10000000:
                # 제일 작은수로 나눴을 때까 가장 큰 수가 될테니깐 나눠지면 바로 break
                k = i//j  # j가 2부터 커지기 때문에 처음 만나는 i//j가 약수 중 가장 큰 값
                break
        answer.append(k)

    return answer


k = int(3 != 1)  # i가 1이면 0, 1이 아니면 1을 대입
print(k)
