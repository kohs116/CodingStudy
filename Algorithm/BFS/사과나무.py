from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
a = list(map(int, input().split()) for _ in range(n))
ch = [[0] * n for _ in range(n)]  # 방문 여부 확인
sum = 0  # 출력할 값
Q = deque()
ch[n // 2][n // 2] = 1  # 중앙 지점 check
sum += a[n // 2][n // 2]  # 중앙 지점 값 누적
Q.append((n // 2, n // 2))
L = 0  # Level 0
while True:
    if L == n // 2:
        break
    size = len(Q)
    for i in range(size):
        tmp = Q.popleft()
        for j in range(4):  # 상하좌우
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]
            if ch[x][y] == 0:
                sum += a[x][y]
                ch[x][y] = 1  # check
                Q.append((x, y))
    L += 1
print(sum)
