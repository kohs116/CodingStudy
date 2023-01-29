# 각 행의 합, 열의 합, 두 대각선의 합 중 가장 큰 합 출력

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

largest = -2147000000
for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += a[i][j]  # 행의 합 (행 고정)
        sum2 += a[j][i]  # 열의 합 (열 고정)
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2
sum1 = sum2 = 0
for i in range(n):
    sum1 += a[i][i]  # 대각선1
    sum2 += a[i][n - i - 1]  # 대각선2
if sum1 > largest:
    largest = sum1
if sum2 > largest:
    largest = sum2
print(largest)