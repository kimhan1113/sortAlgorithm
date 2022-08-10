import re
import sys


def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True


name = "안녕하세요 반갑습니다 ㅋㅋabc"
recompile = re.compile('[^a-zA-Z가-힣+]')

result = recompile.sub('', name)
# print(result)

print(sys.platform)
