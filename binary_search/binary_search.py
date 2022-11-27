def binary_search(arr, target, start, end):

    if start > end:
        return False

    mid = (start + end) // 2

    if arr[mid] == target:
        return True

    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)

    else:
        return binary_search(arr, target, mid + 1, end)


arr = [1,3,5,8,11,12,18,20]

answer = binary_search(arr, 19, 0, len(arr)-1)
print(answer)