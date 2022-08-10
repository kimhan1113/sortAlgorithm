
numbers = [100, 101, 102, 103, 104]
start = [1, 2]
finish = [2, 4]

# def range_sum(start, finish, n):

#     answer = n * (start + finish) // 2
#     return answer

def solution(numbers, start, finish):

    answer = []

    for s, f in zip(start, finish):

        numbers[s:f]

        answer.append(range_sum(numbers[s], numbers[f], f-s+1))

    return answer



answer = solution(numbers, start, finish)
print(answer)