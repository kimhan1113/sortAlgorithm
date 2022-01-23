import collections as col


def solution(participant, completion):
    hashDict = {}
    sumHash = 0

    for part in participant:
        hashDict[hash(part)] = part
        sumHash += hash(part)

    for comp in completion:
        sumHash -= hash(comp)

    print(hashDict[sumHash])


solution(["marina", "josipa", "nikola", "vinko", "filipa"],
         ["josipa", "filipa", "marina", "nikola"])
# print(a)


def solution_(part, com):

    answer = col.Counter(part) - col.Counter(com)
    return list(answer.keys())[0]
