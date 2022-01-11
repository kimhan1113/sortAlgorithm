import math


def solution(progresses, speeds):
    answer = []
    progresses = [math.ceil((100-a)/b) for a, b in zip(progresses, speeds)]
    front = 0

    for idx in range(len(progresses)):
        if progresses[front] < progresses[idx]:
            answer.append(idx-front)
            front = idx

    answer.append(len(progresses)-front)
    return answer
