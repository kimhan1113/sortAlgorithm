

from math import dist
import sys

input = sys.stdin.readline
INF = int(1e9)
# 무한을 의미하는 10억

# 노드의 개수 간선의 개수
n, m =map(int, input().split())

# 시작 노드 번호
start = int(input())

# 각 노드에 연결되어 있는 노드 정보 담는 리스트
graph = [[] for _ in range(n+1)]

# 방문한 적 이 있는지 체크하는 리스트
visited = [False] * (n+1)

# 최단 거리 테이블 무한으로 초기화
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    # a 노드에서 b노드까지 가는데 비용이  c
    graph[a].append((b,c))


# 방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i

    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(n-1)    :

        now = get_smallest_node()
        visited[now] = True

        for j in graph[now]:
            cost = distance[now] + j[1]

            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)                


for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")

    else:
        print(distance[i])    
