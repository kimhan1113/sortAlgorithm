def solution(s):
    answer = len(s)

    for unit in range(1, len(s) // 2 + 1):
        zip_s = ''
        start = 0
        num = 1
        while start + unit <= len(s):
            sub = s[start: start + unit]
            
            while sub == s[start + unit * num: start + unit * (num + 1)]:
                num += 1
            if num > 1:
                zip_s += str(num)
            zip_s += sub
            start += unit * num
            num = 1

        zip_s += s[start:]
        answer = min(answer, len(zip_s))    


    return answer


def solution(s):
    answer = len(s)

    for unit in range(1, len(s) // 2 + 1):
        zip_len = 0
        start = 0
        num = 1
        while start + unit <= len(s):
            sub = s[start: start + unit]
            
            while sub == s[start + unit * num: start + unit * (num + 1)]:
                num += 1
            if num > 1:
                zip_len += len(str(num))
            zip_len += len(sub)
            start += unit * num
            num = 1

        zip_len += len(s) - start
        answer = min(answer, zip_len)    


    return answer    