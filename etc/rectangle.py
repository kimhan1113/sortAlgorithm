
from collections import Counter


a = [[1,4], [3,4], [3,10]]

answer = []

x = Counter(list(zip(*a))[0])
y = Counter(list(zip(*a))[1])

print(sorted(y.elements()))

answer = [sorted(x.elements())[0] , sorted(y.elements())[0]]
# print(answer)

x_point = 0
y_point = 0

for (key1, value1),(key2,value2) in zip(x.items(), y.items()):
 
    if value1 == 1:
        x_point = key1

    if value2 == 1:
        y_point = key2


# print(x_point, y_point)
answer = [x_point, y_point]
# print(answer)
# print(Counter(y))

# print(list(Counter(x).keys()))
# # print(list(Counter(y).keys())[1])