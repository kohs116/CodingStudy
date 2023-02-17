dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(X, Y):
    global cnt
    if X == 6 and Y == 6:
        cnt += 1
    else:
        for i in range(4):
            xx = X + dx[i]
            yy = Y + dy[i]
            if 0 <= xx <= 6 and 0 <= yy <= 6 and miro[xx][yy] == 0:
                miro[xx][yy] = 1  # check
                DFS(xx, yy)
                miro[xx][yy] = 0  # back


if __name__ == "__main__":
    miro = [list(map(int, input().split())) for _ in range(7)]
    cnt = 0
    miro[0][0] = 1
    DFS(0, 0)
    print(cnt)
