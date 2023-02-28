from collections import deque

n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
degree = [0] * (n + 1)  # 진입 차수
dq = deque()
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1  # 방향 그래프
    degree[b] += 1  # 차수 증가
for i in range(1, n + 1):
    if degree[i] == 0:  # 차수가 0이라면
        dq.append(i)
while dq:
    x = dq.popleft()
    print(x, end=' ')
    for i in range(1, n + 1): # 차수 감소
        if graph[x][i] == 1:
            degree[i] -= 1
            if degree[i] == 0:
                dq.append(i)
