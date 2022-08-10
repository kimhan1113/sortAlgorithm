
from collections import defaultdict
from functools import cmp_to_key

# words = [
#     'but',
#     'i',
#     'wont',
#     'hesitate',
#     'no',
#     'more',
#     'no',
#     'more',
#     'it',
#     'cannot',
#     'wait',
#     'im',
#     'yoursi',
#     'am',
# ]

words = []
n = int(input())

dic = defaultdict(list)

for i in range(n):
    word = input()
    if not word in dic:
        dic[word] = [len(word), word]


result = sorted(dic.items(), key=lambda x: (x[1][0], x[1][1]))

for word in result:
    print(word[1][1])

# for i in range(1, len(words)):
#     if len(words[i-1]) > len(words[i]):
#         sort_words.appendleft(words[i])
#     elif len(words[i-1]) < len(words[i]):
#         sort_words.append(words[i])
#     else:
#         if words[i-1] > words[i]:
#             sort_words.appendleft(words[i])
#         else:
#             sort_words.append(words[i])

# print(sort_words)
