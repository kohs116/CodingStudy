n, m = map(int, input().split())  # n: 정점번호 m: 간선 개스
dis = [[5000] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):  # 자기자신에서 자기자신으로 가는 것 초기화
    dis[i][i] = 0
for i in range(m):  # 직행하는 값 초기화
    a, b, c = map(int, input().split())
    dis[a][b] = c
for k in range(1, n + 1):  # 플로이드 와샬
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
    for i in range(1, n + 1):  # 출력
        for j in range(1, n + 1):
            if dis[i][j] == 5000:
                print("M", end=' ')
            else:
                print(dis[i][j], end=' ')
