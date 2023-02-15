def DFS(L, pay):
    global res
    if L == n+1:
        if pay > res:
            res = pay
    else:
        if L+T[L]<=n+1: # L(현재 날짜) + 그 날 상담 하면서 소요되는 날짜
            DFS(L + T[L], pay + P[L])
        DFS(L + 1, pay)

if __name__ == "__main__":
    n = int(input())  # 남은 N일 동안 최대한 많은 상담
    T = list()
    P = list()
    for i in range(n):
        a,b = map(int,input().split())
        T.append(a)
        P.append(b)

    res = -2147000000
    T.insert(0,0) # 인덱스를 날짜(일)로 설정할거라 0번에는 0 insert
    P.insert(0,0)
    DFS(1, 0)
    print(res)
