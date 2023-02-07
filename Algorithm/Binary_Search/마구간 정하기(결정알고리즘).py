# 가장 가까운 두 말의 최대거리를 이분검색
def Count(len):
    cnt = 1
    ep = Line[0]  # 첫번째 마구간
    for i in range(1, n):
        if Line[i] - ep >= len:
            cnt += 1
            ep = Line[i]
    return cnt


n, c = map(int, input().split())
Line = []
for _ in range(n):
    tmp = int(input())
    Line.append(tmp)
Line.sort() # 1 2 4 8 9
lt = 1
rt = Line[n - 1] # 9
while lt <= rt:
    mid = (lt + rt) // 2 # 5
    if Count(mid) <= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(res)