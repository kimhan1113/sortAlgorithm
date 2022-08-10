

def solution(s):

    count = 0
    for i in range(0, len(s)):
        if s[i] == "(":
            count += 1
        else:
            count -= 1
            if count < 0:
                return False

    if count != 0:
        return False

    return True


s = ")()("
answer = solution(s)


print(answer)



