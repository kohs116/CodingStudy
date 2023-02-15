# N개의 문제를 풀려고 한다.
# 문제를 풀었을 때 얻는 점수, 푸는데 걸리는 시간이 주어짐
# 제한시간 M안에 N개의 문제 중 최대점수를 얻을 수 있도록 해야함
# 최대점수 출력
def DFS(L, sum, time):
    global res
    if time > m:  # 시간제한 넘어가면
        return  # 가지치기
    if L == n:
        if sum > res:
            res = sum
    else:
        DFS(L + 1, sum + pv[L], time + pt[L])  # 풀었을 때
        DFS(L + 1, sum, time)  # 안 풀었을 때


if __name__ == "__main__":
    n, m = map(int, input().split())
    pv = list()
    pt = list()
    for _ in range(n):
        score, time = map(int, input().split())
        pv.append(score)
        pt.append(time)
    res = -2147000000
    DFS(0, 0, 0)
    print(res)
