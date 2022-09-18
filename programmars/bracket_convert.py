

def solution(p):
    if not p:
        return p

    def split(w):
        cnt_open, cnt_close = 0, 0
        for i, ch in enumerate(w):
            if ch == "(":
                cnt_open += 1
            elif ch == ")":
                cnt_close += 1
            if cnt_open == cnt_close:
                return w[:i+1], w[i+1:]

    def is_valid(s):
        cnt_open, cnt_close = 0, 0
        for ch in s:
            if ch == "(":
                cnt_open += 1
            elif ch == ")":
                cnt_close += 1
            if cnt_close > cnt_open:
                return False

        return True


    def reverse_bracket(u):

        result = []

        for b in u:
            if b == "(":
                result.append(")")
            else:
                result.append("(")    

        return "".join(result)

    answer = ""
    v = p

    while v:

        u, v = split(v)

        if is_valid(u):
            answer += u

        else:
            return answer + '(' + solution(v) + ')' + reverse_bracket(u[1:-1])

    return answer


p = "()))((()"
answer = solution(p)
print(answer)


# 문자열 p를 u, v로 분리하는 함수
def divide(p):
    open_p = 0
    close_p = 0

    for i in range(len(p)):
        if p[i] == '(':
            open_p += 1
        else:
            close_p += 1
        if open_p == close_p:
            return p[:i + 1], p[i + 1:]


# 문자열 u가 올바른 괄호 문자열인지 확인하는 함수
def check(u):
    stack = []

    for p in u:
        if p == '(':
            stack.append(p)
        else:
            if not stack:
                return False
            stack.pop()

    return True


def solution(p):
    # 과정 1
    if not p:
        return ""

    # 과정 2
    u, v = divide(p)

    # 과정 3
    if check(u):
        # 과정 3-1
        return u + solution(v)
    # 과정 4
    else:
        # 과정 4-1
        answer = '('
        # 과정 4-2
        answer += solution(v)
        # 과정 4-3
        answer += ')'

        # 과정 4-4
        for p in u[1:-1]:
            if p == '(':
                answer += ')'
            else:
                answer += '('

        # 과정 4-5
        return answer