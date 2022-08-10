import sys


n, m = map(int, sys.stdin.readline().split())
conn = [[] for i in range(n+1)]
cnt_incoming = [0 for i in range(n+1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    conn[a].append(b)
    cnt_incoming[b] += 1

answer = []
for node in range(1, n+1):
    if cnt_incoming[node] == 0:
        answer.append(0)
        for nextnode in conn[node]:
            cnt_incoming[nextnode] -= 1
