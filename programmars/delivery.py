import heapq


def dijkstra(dis, ajd):
    heap = []
    heapq.heappush(heap, [0,1])

    while heap:
        cost, node = heapq.heappop(heap)
        for c, n in ajd[node]:
            if cost + c < dis[n]:
                dis[n] = cost + c
                heapq.heappush(heap, [cost+c, n])

def solution(N, road, K):
    INF = int(1e9)
    dis = [INF] * (N+1)
    dis[1] = 0
    adj = [[] for _ in range(N+1)]

    for r in road:
        adj[r[0]].append([r[2], r[1]])
        adj[r[1]].append([r[2], r[0]])

    print(adj)    

    dijkstra(dis, adj)    
    return len([x for x in dis if x <= K])


N = 5	
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]	
K = 3	
result = 4

answer = solution(N, road, K)
print(answer)
		