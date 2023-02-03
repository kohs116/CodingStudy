# 1 2 3 중에 중복을 허용하여 뽑기 - 12 13 21 22 23 ...
def DFS(L):
    global cnt
    if L==n:
        for j in range(m):
            print(res[j], end=' ')
        print()
        cnt += 1
    else:
        for i in range(1,n+1): # i는 1부터 n
            res[L]=i
            DFS(L+1)

if __name__ == "__main__":
    n,m=map(int,input().split())
    res=[0]*m
    cnt=0 # 개수 출력
    DFS(0)
    print(cnt)