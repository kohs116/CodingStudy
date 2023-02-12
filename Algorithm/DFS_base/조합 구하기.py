def DFS(L, s):
    global ch, cnt
    if L == m:
        for i in range(m):
            print(res[i], end=' ')
        cnt += 1
        print()

    else:
        for j in range(s, n + 1):
            res[L] = j
            DFS(L + 1, j + 1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * (n + 1)
    cnt = 0
    DFS(0, 1)
    print(cnt)
