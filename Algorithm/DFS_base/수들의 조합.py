def DFS(L, s, sum):
    global cnt
    if L == k:
        for j in range(m):
            if sum % m == 0:
                cnt += 1
                print(cnt)
    else:
        for i in range(s, n):  # a라는 리스트에 0~n-1 들어가있음
            DFS(L + 1, i + 1, sum + a[i])


if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    m = int(input())
    cnt = 0
    DFS(0, 0, 0)
    print(cnt)
