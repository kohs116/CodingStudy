n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)  # 첫 항이 index 1부터 시작할 수 있도록
dy = [0] * (n + 1)
dy[1] = 1
res = 0
for i in range(2, n + 1):
    max = 0
    for j in range(i - 1, 0, -1):  # i-1 ~ 1
        if arr[j] < arr[i] and dy[j] > max:
            max = dy[j]  # arr[j]가 마지막 항인 수열의 길이
    dy[i] = max + 1

    if dy[i] > res:
        res = dy[i]
print(res)
