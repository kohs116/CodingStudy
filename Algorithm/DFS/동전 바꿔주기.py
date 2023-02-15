def DFS(L, sum):
    global cnt
    if sum > t:
        return
    if L == k:
        if sum == t:
            cnt += 1
    else:
        for i in range(v[L] + 1):
            DFS(L + 1, sum + (i * a[L]))


if __name__ == "__main__":
    t = int(input())  # 지폐 금액
    k = int(input())  # 동전 가지 수
    a = []  # 동전 금액 넣을 리스트
    v = []  # 동전 개수 넣을 리스트
    for _ in range(k):
        p, n = map(int, input().split())
        a.append(p)
        v.append(n)
    cnt = 0
    DFS(0, 0)
    print(cnt)
