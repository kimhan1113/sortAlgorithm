from itertools import combinations
from collections import Counter, defaultdict


orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,5]
result = ["AC", "ACDE", "BCFG", "CDE"]   

def solution(orders, course):

    ordered = []

    for order in orders:
        ordered.append("".join(sorted(order)))

    answer = []
    comb = []

    for order in ordered:
        c = list(order)
        for i in range(2, len(c)+1):

            for j in list(combinations(c, i)):
                comb.append(j)


    # 길이 : 최고주문횟수
    max_len = defaultdict(int)

    for c in course:
        for key, value in Counter(comb).items():
            if len(key) == c and max_len[len(key)]:
                if max_len[len(key)] < value:
                    max_len[len(key)] = value

            elif len(key) == c:
                max_len[len(key)] = value

    # print(sorted(Counter(comb).items(), key=lambda x:(x[1], len(x[0])), reverse=True))
    # assert 1==0

    for c in course:
        for key, value in Counter(comb).items():

            if len(key) == c and value == max_len[len(key)] and value > 1:
                answer.append("".join(key))

    return sorted(answer)


answer = solution(orders, course)
print(answer)






# print(list(c))



# for char in list(combinations(c, len(c))):
#     comb.append(char)

# print(comb)
