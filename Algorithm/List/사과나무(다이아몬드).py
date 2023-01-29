# 격자판의 다이아몬드 모양 부분 합

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
res = 0
start = end = n // 2 #중간 열 부터 시작
for i in range(n):
    for j in range(start, end + 1):
        res += a[i][j]
    if i < n // 2: #구간 넓히기
        start -= 1
        end += 1
    else: # 구간 좁히기
        start += 1
        end -= 1
print(res)
