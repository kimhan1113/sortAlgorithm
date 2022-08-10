
def solution(n):

    array_ = ["1", "2", "4"]
    answer = ''

    while(n > 0):
        n = n-1
        answer = array_[n % 3] + answer
        n //= 3

    return answer


answer = solution(10)
print(answer)
