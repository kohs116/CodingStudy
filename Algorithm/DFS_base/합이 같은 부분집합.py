# 전체 원소의 합 total - 부분집합1 합 sum = 부분집합2 합 sum
# sum이 total//2 보다 커지면 더 이상 진행할 필요 없어짐

import sys
def DFS(L, sum):  # L:a의 인덱스
    if sum>total//2:
        return
    if L == n:
        if sum == (total - sum):
            print('YES')
            sys.exit(0)  # 프로그램 종료
    else:
        DFS(L + 1, sum + a[L])
        DFS(L + 1, sum)


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    DFS(0, 0)
    print("NO")
