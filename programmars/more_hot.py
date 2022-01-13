from collections import deque
import heapq


def solution(scoville, K):

    heap = []

    for num in scoville:
        heapq.heappush(heap, num)

    answer = 0

    if heap[0] >= K:
        return answer

    for i in range(len(heap)-1):
        heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        answer += 1
        if heap[0] >= K:
            return answer
    answer = -1
    return answer


scoville = [1, 2, 3, 9, 10, 12]
# ans = solution(scoville, 7)

heap = [4, 1, 7, 3, 8, 5]
heapq.heapify(heap)
print(type(heap))
