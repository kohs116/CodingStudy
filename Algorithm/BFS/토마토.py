from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())  # m은 상자의 가로 칸 수, n은 상자의 세로 칸 수
board = [list(map(int, input().split())) for _ in range(m)]
dis = [[0] * n for _ in range(m)]
dq = deque()
for i in range(m):
    for j in range(n):
        if board[i][j] == 1:
            dq.append((i, j))
while dq:
    tmp = dq.popleft()
    for k in range(4):
        x = tmp[0] + dx[k]
        y = tmp[1] + dy[k]
        if 0 <= x < m and 0 <= y < n and board[x][y] == 0:
            board[x][y] = 1
            dis[x][y] = dis[tmp[0]][tmp[1]] + 1
            dq.append((x, y))
flag = 1
for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            flag = 0
result = 0
if flag == 1:
    for i in range(m):
        for j in range(n):
            if dis[i][j] > result:
                result = dis[i][j]
    print(result)
else:
    print(-1)
