
n = 6
arr1 = [60, 33, 33, 22, 31, 50]
arr2 = [27, 56, 19, 14, 14, 10]

# n = 5
# arr1 = [9, 20, 28, 18, 11]
# arr2 = [30, 1, 21, 17, 28]


# start = len(str(bin(v))) - n

# print(str(bin(v))[start:].replace('b', '0'))


def make_binary(v, n):
    start = len(str(bin(v))) - n

    return str(bin(v))[start:].replace('b', '0').zfill(n)

# def make_binary(v, n):

#     return str(bin(v)).replace('b', '0').zfill(n)


# def solution(n, arr1, arr2):

#     answer = []

#     arr1_map = []
#     arr2_map = []

#     for value1, value2 in zip(arr1, arr2):
#         arr1_map.append(make_binary(value1, n))
#         arr2_map.append(make_binary(value2, n))

#     print(arr1_map, arr2_map)

#     for value1, value2 in zip(arr1_map, arr2_map):
#         temp = []
#         for i in range(len(value1)):
#             if value1[i] == str(0) and value2[i] == str(0):
#                 temp.append(" ")
#             else:
#                 temp.append("#")
#         answer.append("".join(temp))

#     return answer


# answer = solution(n, arr1, arr2)
# print(answer)
n = 6
arr1 = [60, 33, 33, 22, 31, 50]
arr2 = [27, 56, 19, 14, 14, 10]


def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        tmp = bin(arr1[i] | arr2[i])
        print(tmp)
        # tmp결과 ex) '0b1101'
        tmp = tmp[2:].zfill(n)
        # tmp결과 ex) '01101'
        tmp = tmp.replace('1', '#').replace('0', ' ')
        # tmp결과 ex) ' ## #'
        answer.append(tmp)

    return answer


answer = solution(n, arr1, arr2)
# print(answer)
