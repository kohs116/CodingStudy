n = int(input())
arr = list(map(int, input().split()))
dy = [0] * (n + 1)
dy[1] = 1
res = 0
arr.insert(0, 0)
for i in range(2, n + 1):
    max = 0
    for j in range(i - 1, 0, -1):
        if arr[j] < arr[i] and dy[j] > max:
            # dy[j]>max 를 하는 이유는 연결 해 놓은 선들의 최대 값을 판별하기 위해
            max = dy[j]
    dy[i] = max + 1
    if dy[i] > res:
        res = dy[i]
print(res)
