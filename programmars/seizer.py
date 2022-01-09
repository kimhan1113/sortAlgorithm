from string import ascii_lowercase, ascii_uppercase


lower = ascii_lowercase
upper = ascii_uppercase


def solution(strings, num):

    answer = []

    for i, string in enumerate(strings):
        if string.isupper():
            index = upper.find(string)
            index = (index + num) % 26
            answer.append(upper[index])
        elif string.islower():
            index = lower.find(string)
            index = (index + num) % 26
            answer.append(lower[index])
        else:
            answer.append(" ")

    ans = ''.join(answer)
    return ans
