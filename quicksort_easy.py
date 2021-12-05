

def partition(arr, l, r):
    pivot = arr[r]
    i = l-1

    for j in range(l, r):
        if(arr[j] <= pivot):
            i = i+1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1


def quicksort(arr, l, r):

    if(l < r):
        p = partition(arr, l, r)

        quicksort(arr, l, p-1)
        quicksort(arr, p+1, r)


arr = [1, 5, 7, 3, 2, 6, 9, 8, 4, 11, 15]

# quicksort(arr, 0, len(arr)-1)
# print(arr)


def partions(arr, l, r):
    if(l < r):
        pivot = arr[r]
        i = l-1
        for j in range(l, r):
            if(arr[j] <= pivot):
                i = i+1
                arr[j], arr[i] = arr[i], arr[j]

        arr[i+1], arr[r] = arr[r], arr[i+1]
        return i+1


def quicksort_(arr, l, r):

    if(l < r):
        p = partions(arr, l, r)
        quicksort_(arr, l, p-1)
        quicksort_(arr, p+1, r)


quicksort_(arr, 0, len(arr)-1)
print(arr)
