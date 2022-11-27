
from random import randint
import time

array = [1,2,3,7,2,1,8,2,10]

# for _ in range(10000):
#     array.append(randint(1,100))

# start_time = time.time()

# for i in range(len(array)):
#     min_index = i
#     for j in range(i + 1, len(array)):
#         if array[min_index] > array[j]:
#             min_index = j

#     array[i], array[min_index] = array[min_index], array[i]

# end_time = time.time()

# print(end_time - start_time)




for i in range(len(array)):
    min_index = i
    for j in range(i, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[min_index], array[i] = array[i], array[min_index]

print(array)    