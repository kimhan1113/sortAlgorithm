def solution(s):
    answer = 0

    half_length = len(s) // 2 + 2
    d_length = 1

    while(d_length < half_length):

        temp = 1
        str_list = []
        for i in range(0, len(s), d_length):
            if(s[i:i+d_length] == s[i+d_length:(i+d_length)+d_length]):
                temp += 1
            else:
                if temp == 1:
                    str_list.append(s[i:i+d_length])
                else:
                    str_list.append(str(temp)+s[i:i+d_length])
                    temp = 1

        total_list = "".join(str_list)
        if d_length == 1:
            answer = len(total_list)
        else:
            if answer > len(total_list):
                answer = len(total_list)
        d_length += 1

    return answer


ans = solution("abcabcabcabcdededededede")
print(ans)
