temp = []

def check_bracket(bracket):

    count = 0

    if bracket[0] == ")" or bracket[-1] == "(":
        return False

    for b in bracket:
        if b == "(":
            count += 1

        else:
            count -= 1
            if count < 0:
                return False

    if count == 0:
        return True

    return False    

# 무조건 균형잡힌 괄호가 들어오니깐 짝수만들어옴
def convert_braket(braket):

    if braket == ")(":
        return "()"

    temp = braket[1:-1]

    convert = ""

    for b in temp:
        if b == "(":
            convert += ")"
        else:
            convert += "(" 

    return "(" + convert + ")"


def divide_braket(braket):

    count = 0

    if braket == "":
        return
    
    for i, b in enumerate(braket):
        if b == "(":
            count += 1
            if count == 0:

                u = braket[:i+1]
                v = braket[i+1:]

                if check_bracket(u):
                    temp.append(u) # u
                    if len(v) != 0:
                        divide_braket(v)

                else:
                    temp.append(convert_braket(u))
                    if len(v) != 0:
                        divide_braket(v)
               
        else:
            count -= 1
            if count == 0:
                u = braket[:i+1]
                v = braket[i+1:]

                if check_bracket(u):
                    temp.append(u) # u
                    if len(v) != 0:
                        divide_braket(v)

                else:
                    temp.append(convert_braket(u))
                    if len(v) != 0:
                        divide_braket(v)


def solution(p):
    answer = ''

    divide_braket(p)

    answer = "".join(temp)
    return answer


braket = ")()())(("

answer = solution(braket)
print(answer)


