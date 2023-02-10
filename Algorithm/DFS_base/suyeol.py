import sys

def DFS(L, sum):
    if L == n and sum == f:
        for x in p:
            print(x, end=' ')
        sys.exit(0)  # 프로그램 종료
    else:
        for i in range(1, n + 1):  # 1~4
            if ch[i] == 0:
                ch[i] = 1
                p[L] = i
                DFS(L + 1, sum + (p[L] * b[L]))
                ch[i] = 0

if __name__ == "__main__":
    n, f = map(int, input().split())
    b = [1] * n  # 계수 -> 양 끝 값의 계수는 1로 고정
    p = [0] * n  # 순열
    ch = [0] * (n + 1)  # 중복을 방지하기 위함
    for i in range(1, n):  # 제일 첫번째와 마지막은 1로 고정
        b[i] = (b[i - 1] * (n - i)) // i  # 계수 초기화
    DFS(0, 0)
