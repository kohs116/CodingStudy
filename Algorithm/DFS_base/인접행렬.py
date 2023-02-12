n, m = map(int, input().split())  # n=노드번호 m=간선 개수
g = [[0] * (n + 1) for _ in range(n + 1)]  # 인접행렬 그래프
for i in range(m):
    a, b, c = map(int, input().split())  # 간선 정보 입력
    g[a][b] = c

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(g[i][j], end=' ')
    print()
