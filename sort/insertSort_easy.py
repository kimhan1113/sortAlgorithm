
arr_list = [1, 5, 23, 6, 7, 8, 1, 76, 8]


def insertSort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while(j >= 0 and arr[j] > key):
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key
    return arr


arr = insertSort(arr_list)
print(arr)



for i in range(1, len(arr_list)):
    for j in range(i, 0, -1):
        if arr_list[j] > arr_list[j-1]:
            arr_list[j], arr_list[j-1] = arr_list[j-1], arr_list[j]
        else:
            break    