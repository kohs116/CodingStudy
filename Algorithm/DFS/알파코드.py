def DFS(L, p):
    global cnt, res
    if L == n:
        cnt += 1
        for j in range(p):
            print(chr(res[j] + 64), end='')
        print()

    else:
        for i in range(1, 27):
            if code[L] == i:  # 자릿수
                res[p] = i
                DFS(L + 1, p + 1)
            elif i >= 10 and code[L] == i // 10 and code[L + 1] == i % 10:
                res[p] = i
                DFS(L + 2, p + 1)


if __name__ == "__main__":
    code = list(map(int, input()))
    n = len(code)
    code.insert(n, -1)  # n+1까지 판별
    cnt = 0
    res = [0] * (n + 3)  # 공간 넉넉하게 잡기 위함, 특별히 3인 이유는 없음
    DFS(0, 0)
    print(cnt)
