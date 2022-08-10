import re

# def solution(dartResult):

#     eval_num = ""

#     for i in range(0, len(dartResult)):

        


#         if dartResult[i].isnumeric() and i != 0:
#             if dartResult[i+1].isnumeric():
#                 eval_num += "+" + str(dartResult[i:i+2])
#             else:
#                 eval_num += "+" + str(dartResult[i])

#         elif dartResult[i].isnumeric() and i == 0:
#             if dartResult[i+1].isnumeric():
#                 eval_num += str(dartResult[i:i+2])
#             else:
#                 eval_num += str(dartResult[i])

#         elif dartResult[i] == "S":
#             eval_num += "**1"
#         elif dartResult[i] == "D":
#             eval_num += "**2"
#         elif dartResult[i] == "T":
#             eval_num += "**3"

#         elif dartResult[i] == "*":
#             eval_list = eval_num.split("+")
#             # print(eval_list)
#             if len(eval_list) == 1:
#                 eval_num += "*2"
#             elif len(eval_list) == 2:
#                 eval_num = eval_num.split("+")[0] + "*2" + "+" + eval_num.split("+")[1] + "*2"
#             else:
#                 eval_num = eval_num.split("+")[0] + "+" + eval_num.split("+")[1] + "*2" + "+" + eval_num.split("+")[2] + "*2"

#         elif dartResult[i] == "#":
#             # eval_num = eval_num.split("+")[0] + "*-2" + "+" + eval_num.split("+")[1] + "*-2"
#             eval_num += "*-1"

#     print(eval_num)
#     answer = eval(eval_num)
#     return answer


# def solution(dartResult):



#     eval_num = ""

#     for i in range(0, len(dartResult)):
#         if dartResult[i].isnumeric():
#             eval_num += dartResult[i]

#         elif dartResult[i] == "S":
#             if not dartResult[i+1] == "*" or dartResult[i+1] == "#":
#                 eval_num += "**1+"
#             else:
#                 eval_num += "**1"    

#         elif dartResult[i] == "D":
#             if not dartResult[i+1] == "*" or dartResult[i+1] == "#":
#                 eval_num += "**2+"
#             else:
#                 eval_num += "**2"    
#             # eval_num = eval(eval_num)

#         elif dartResult[i] == "T":
#             if not dartResult[i+1] == "*" or dartResult[i+1] == "#":
#                 eval_num += "**3+"
#             else:
#                 eval_num += "**3"    
#             # eval_num = eval(eval_num)

#         elif dartResult[i] == "*":
#             eval_num = str(eval_num) + "*2" + "+"

#         elif dartResult[i] == "#":
#             eval_num = str(eval_num) + "*-1" + "+"

#     answer = eval(eval_num)
#     return answer    

# dartResult = "10D*20S#30T*"
# answer = solution(dartResult)
# print(answer)


# def solution(dartResult):
#     n = ''
#     score = []
#     for i in dartResult:
#         if i.isnumeric():
#             n += i
#         elif i == 'S':
#             n = int(n)**1
#             score.append(n)
#             n = ''
#         elif i == 'D':
#             n = int(n)**2
#             score.append(n)
#             n = ''
#         elif i == 'T':
#             n = int(n)**3
#             score.append(n)
#             n = ''
#         elif i == '*':
#             if len(score) > 1:
#                 score[-2] = score[-2] * 2
#                 score[-1] = score[-1] * 2
#             else:
#                 score[-1] = score[-1] * 2
#         elif i == '#':
#             score[-1] = score[-1] * -1
        
#     return sum(score)


def solution():
    n = ""
    answer = []

    for i in dartResult:
        if i.isnumeric():
            n += i

        elif i == "S":
            n = int(n) ** 1
            answer.append(n)
            n = ""

        elif i == "D":
            n = int(n) ** 2
            answer.append(n)
            n = ""

        elif i == "T":
            n = int(n) ** 3
            answer.append(n)
            n = ""     

        elif i == "*":

            if len(answer) > 1:
                answer[-2] = answer[-2] * 2
                answer[-1] = answer[-1] * 2

            else:
                answer[-1] = answer[-1] * 2

        else:
            answer[-1] = answer[-1] * -1

    return sum(answer)



# answer = solution(dartResult)
# print(answer)

dartResult = "1S*2T*3S"

def solution(dartResult):
    number = re.findall("\d{1,2}" , dartResult)
    answer = list(map(int, number))
    strings = re.findall("[A-Z]?[\*\#]|[A-Z]{1}" , dartResult)

    dic = {"S" : 1, "D" : 2, "T": 3}

    for i, text in enumerate(strings):
 
        # 자른 문자열에 옵션이 없다면 그대로 계산
        if len(text) == 1:

            answer[i] = answer[i] ** dic[text]

        # 자른 문자열에 옵션이 있다면 옵션대로 계산
        else:

            if text[-1] == "*":

                # 두번째 인덱스부터는 이전 인덱스 요소도 같이 계산
               
                if i != 0:
                    answer[i-1] = answer[i-1] * 2
                    answer[i] = answer[i] ** dic[text[0]] * 2

                # 첫번째 인덱스 일경우는 첫번째 요소만 계산    
                else:
                    answer[i] = answer[i] ** dic[text[0]] * 2

            # #일경우는 그냥 자기 요소만 계산
            else:
                answer[i] = answer[i] ** dic[text[0]] * -1

    return sum(answer)
        

answer = solution(dartResult)
print(answer)        