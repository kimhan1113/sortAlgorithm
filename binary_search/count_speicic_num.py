from bisect import bisect_left, bisect_right


def count_by_range(arr, x, y):
    left = bisect_left(arr, x)
    right = bisect_right(arr, y)

    return right - left


arrs = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 4, 5, 6, 6]

num = 9
count_num = count_by_range(arrs, num, num)

if count_num == 0:
    print(-1)

else:
    print(count_num)
