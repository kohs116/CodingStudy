def DFS(x, y):
    if dy[x][y] > 0:
        return dy[x][y]
    if x == 0 and y == 0:
        return arr[0][0]
    else:
        if y == 0:  # 행 변화 X
            dy[x][y] = DFS(x - 1, y) + arr[x][y]
        elif x == 0:  # 열 변화 X
            dy[x][y] = DFS(x, y - 1) + arr[x][y]
        else:  # 가지 뻗기
            dy[x][y] = min(DFS(x - 1, y), DFS(x, y - 1)) + arr[x][y]
        return dy[x][y] # 메모이제이션


if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dy = [[0] * n for _ in range(n)]
    print(DFS(n - 1, n - 1))
