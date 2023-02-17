# BFS도 가능
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def DFS(x, y):
    global cnt
    cnt += 1
    map[x][y] = 0
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx <= n - 1 and 0 <= yy <= n - 1 and map[xx][yy] == 1:
            DFS(xx, yy)  # 좌표 넘기기


if __name__ == "__main__":
    n = int(input())
    map = [list(map(int, input())) for _ in range(n)]
    home = 0
    res = []
    for i in range(n):
        for j in range(n):
            if map[i][j] == 1:
                cnt = 0  # 단지 발견 될 때마다 0으로 초기화
                DFS(i, j)  # 단지 가지 뻗기
                res.append(cnt)
    print(len(res))
    res.sort()
    for x in res:
        print(x)