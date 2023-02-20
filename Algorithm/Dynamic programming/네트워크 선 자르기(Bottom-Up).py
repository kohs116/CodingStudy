n = int(input())
dy = [0] * (n + 1)
dy[1] = 1
dy[2] = 2  # 직관적 정보
for i in range(3, n + 1):  # 3m~
    dy[i] = dy[i - 1] + dy[i - 2]
print(dy[n])