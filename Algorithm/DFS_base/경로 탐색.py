def DFS(v):  # v는 노드번호
    global cnt
    if v == n:
        cnt += 1
        for x in path:
            print(x, end=' ')
        print()
    else:
        for i in range(1, n + 1):  # n가지 가지뻗기
            if g[v][i] == 1 and ch[i] == 0:
                ch[i] = 1  # check
                path.append(i)  # v에서 이동하는 노드 i
                DFS(i)
                path.pop()  # 넣었던 것 pop()
                ch[i] = 0  # back


if __name__ == "__main__":
    n, m = map(int, input().split())
    g = [[0] * (n + 1) for _ in range(n + 1)]
    ch = [0] * (n + 1)
    for i in range(m):
        a, b = map(int, input().split())
        g[a][b] = 1
    cnt = 0
    path = []  # 경로 출력
    path.append(1)
    ch[1] = 1  # 1번 노드 방문
    DFS(1)
    print(cnt)
