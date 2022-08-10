
def binary_search(array, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    
    else:
        return binary_search(array, target, mid + 1, end)


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)

if result == None:
    print('결과가 존재하지 x')

else:
    print(result + 1)




def binary_search_target(arr:list, target:int, start:int, end:int)->int:
    if start > end:
        return None

    mid = (start+end)//2

    if arr[mid] == target:
        return mid

    elif arr[mid] > target:
        binary_search_target(arr, target, start, mid-1)
    else:
        binary_search_target(arr, target, mid+1, end)



