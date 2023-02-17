dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def DFS(X, Y):
    global cnt
    if X == ex and Y == ey:
        cnt += 1
    else:
        for k in range(4):
            xx = X + dx[k]
            yy = Y + dy[k]
            if 0 <= xx <= n - 1 and 0 <= yy <= n - 1 and ch[xx][yy] == 0 and board[xx][yy] > board[X][Y]:
                ch[xx][yy] = 1  # check
                DFS(xx, yy)
                ch[xx][yy] = 0  # back


if __name__ == "__main__":
    n = int(input())
    board = [[0] * n for _ in range(n)]
    ch = [[0] * n for _ in range(n)]
    max = -2147000000
    min = 2147000000
    for i in range(n):
        tmp = list(map(int, input().split()))
        for j in range(n):
            if tmp[j] < min:
                min = tmp[j]
                sx = i
                sy = j
            if tmp[j] > max:
                max = tmp[j]
                ex = i
                ey = j
            board[i][j] = tmp[j] # tmp 한 줄을 board에 복사

    ch[sx][sy] = 1
    cnt = 0
    DFS(sx, sy)
    print(cnt)
