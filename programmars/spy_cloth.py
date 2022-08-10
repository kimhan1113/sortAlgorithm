import collections as col
from functools import reduce

# https://programmers.co.kr/learn/courses/30/lessons/42578?language=python3


def solution_(clothes):  # 1. 옷을 종류별로 구분하기
    hash_map = {}
    for clothe, type in clothes:
        hash_map[type] = hash_map.get(type, 0) + 1
        print(hash_map)
    # 2. 입지 않는 경우를 추가하여 모든 조합 계산하기
    answer = 1
    for type in hash_map:
        answer *= (hash_map[type] + 1)
    # 3. 아무종류의 옷도 입지 않는 경우 제외하기
    return answer - 1


def solution__(clothes):

    hash_ = {}

    for cloth, type in clothes:
        hash_[type] = hash_.get(type, 0) + 1

    answer = 1

    for type in hash_:
        answer *= (hash_[type] + 1)
    return answer - 1


def solution(cloths):

    counter = col.Counter([type for cloth, type in cloths])
    print(counter.values())
    answer = reduce(lambda acc, cur: acc*(cur+1), counter.values(), 1) - 1
    return answer


solution_([["yellowhat", "headgear"], ["bluesunglasses",
                                       "eyewear"], ["green_turban", "headgear"]])
# print(solution([["yellowhat", "headgear"], ["bluesunglasses",
#                                             "eyewear"], ["green_turban", "headgear"]]))
