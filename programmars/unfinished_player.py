import collections as col
from collections import defaultdict

# https://programmers.co.kr/learn/courses/30/lessons/42576


def solution(participant, completion):
    hashDict = {}
    sumHash = 0

    for part in participant:
        hashDict[hash(part)] = part
        sumHash += hash(part)

    for comp in completion:
        sumHash -= hash(comp)


solution(["marina", "josipa", "nikola", "vinko", "filipa"],
         ["josipa", "filipa", "marina", "nikola"])
# print(a)


def solution_(part, com):

    answer = col.Counter(part) - col.Counter(com)
    # print(col.Counter(part))
    # print(col.Counter(com))
    # return list(answer.keys())[0]


solution_(["marina", "josipa", "nikola", "vinko", "filipa"],
          ["josipa", "filipa", "marina", "nikola"])


participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]


def solution__(participant, completion):
    member = defaultdict(int)

    for part in participant:
        member[part] += 1

    for com in completion:
        member[com] -= 1

    answer = ''
    for i, mem in enumerate(member.values()):
        if mem == 1:
            answer = list(member.keys())[i]
            break

    return answer


mem = solution__(participant, completion)

print(mem)


def solution(participant, completion):

    dic = defaultdict(int)

    for mem in completion:
        dic[mem] -= 1

    for mem in participant:
        dic[mem] += 1

        if dic[mem] > 0:
            return mem
