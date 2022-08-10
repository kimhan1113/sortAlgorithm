

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

result = 0


def dfs(x, y):
    if x <= -1 or y <= -1 or x >= n or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1

        dfs[x][y-1]
        dfs[x-1][y]
        dfs[x+1][y]
        dfs[x][y+1]
        return True
    return False


for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1


# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bev(graph, i, j):

    graph[i][j] = 1

    for i in range(len(dx)):
        nx = dx + i
        ny = dy + j

        if nx >= i or ny >= j or nx < 0 or ny < 0:
            return False

        if graph[nx][ny] == 0:
            graph[nx][ny] = 1
            bev(graph, i+1, j)
            bev(graph, i, j+1)
            bev(graph, i-1, j)
            bev(graph, i, j-1)
        return True

    return False


n, m = map(int, input().split(' '))
graph = []

for i in range(n):
    graph.append(list(map(int, input())))
