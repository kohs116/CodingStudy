def DFS(L, sum, tsum):  # L:인덱스 번호 sum:부분집합의 합
    global result
    if sum + (total - tsum) < result:  # total-tsum = 이미 더해진 무게 ,sum= 앞으로 더해나갈 무게
        return
    if sum > c:  # 무게제한 넘어가면
        return
    if L == n:  # 종착점
        if sum > result:  # 참조 오류로 global 선언 해야함
            result = sum
        else:
            DFS(L + 1, sum + a[L], tsum + a[L])
            DFS(L + 1, sum, tsum + a[L])  # 부분집합 포함 X


if __name__ == "__main__":
    c, n = map(int, input().split())  # 무게제한, 마리수
    a = [0] * n # 무게 리스트
    result = -2147000000
    for i in range(n):
        a[i] = int(input())
    total = sum(a)
    DFS(0, 0, 0)
    print(result)
