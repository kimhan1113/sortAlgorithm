arr_list = [1, 56, 23, 6, 7, 8, 21, 2, 4]


def selectSort(arr):

    for i in range(len(arr)-1):
        min = i
        for j in range(i+1, len(arr)):
            if(arr[j] < arr[min]):
                min = j

        arr[min], arr[i] = arr[i], arr[min]
    return arr


arr = selectSort(arr_list)
print(arr)


for i in range(len(arr_list)):
    min_index = i
    for j in range(i+1, len(arr_list)):
        if arr_list[min_index] > arr_list[j]:
            min_index = j

    arr_list[i], arr_list[min_index] = arr_list[min_index], arr_list[i]

    
