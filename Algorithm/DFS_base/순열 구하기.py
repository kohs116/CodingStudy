def DFS(L):
    global ch, cnt
    if L == m:  # level과 뽑을 숫자 개수가 같다면
        for j in range(m):
            print(res[j], end=' ')
        print()
        cnt += 1
    else:  # 가지 뻗기
        for i in range(1, n + 1):
            if ch[i] == 0:  # 적용 안된 숫자
                ch[i] = 1
                res[L] = i
                DFS(L + 1)
                ch[i] = 0  # 0으로 바꿔 주어야 함


if __name__ == "__main__":
    n, m = map(int, input().split())  # n개의 숫자 중 m개 뽑기
    res = [0] * n
    ch = [0] * (n + 1)
    cnt = 0
    DFS(0)
    print(cnt)  # 경우의 수
