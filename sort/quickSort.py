

# 분할이 수행되는 횟수가 N가 비례하고 , 분할을 하기 위해서 매번 선형 탐색 (N)이 이루어지기 때문에
# 전체 시간복잡도가 O(N**2)


array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8, 10]

def quick_sort(array, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while(left <= right):

        while(left <= end and array[left] <= array[pivot]):
            left += 1

        while(right > start and array[right] >= array[pivot]):
            right -= 1

        if(left > right):
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)


quick_sort(array, 0, len(array)-1)
print(array)



def quicksort__(arr, start, end):

    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while(left<=right):
        while(left<=end and array[left] <= array[pivot]):
            left += 1
        while(right > start and array[right] >= array[pivot]):
            right -=1

        if (left > right):
            arr[right], arr[pivot] = arr[pivot] = arr[right]

        else:
            arr[left], arr[right]  = arr[right], arr[left]    
    quicksort__(arr, start, right -1)
    quicksort__(arr, right+1, end)



array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))