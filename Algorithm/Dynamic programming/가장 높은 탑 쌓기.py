t = int(input())
arr = []
for _ in range(t):
    s, h, w = map(int, input().split())
    arr.append((s, h, w))
arr.sort(reverse=True)
arr.insert(0, 0)
res = 0
dy = [0] * (t + 1)
dy[1] = arr[1][1]

for i in range(2, t + 1):
    max = 0
    for j in range(i - 1, 0, -1):
        if arr[i][2] < arr[j][2] and max < dy[j]:
            # 현재 무게가 앞의 무게보다 가볍다면
            max = dy[j]
    dy[i] = max + arr[i][1]
    if dy[i] > res:
        res = dy[i]

print(res)
