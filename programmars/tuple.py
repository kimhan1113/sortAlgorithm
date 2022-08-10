
from collections import Counter
import re


def solution(s):
    answer = []
    numbers = re.sub(r'[^0-9|^,]', '', s)
    counts = Counter(numbers.split(','))
    counts = sorted(counts.items(), key=lambda i: i[1], reverse=True)

    for count in counts:
        answer.append(int(count[0]))

    return answer


answer = solution("{{20,111},{111}}")
print(answer)
