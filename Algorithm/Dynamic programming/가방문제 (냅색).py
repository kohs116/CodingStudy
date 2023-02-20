n, m = map(int, input().split())
dy = [0] * (m + 1)
for _ in range(n):
    w, v = map(int, input().split())
    for j in range(w, m + 1):
        dy[j] = max(dy[j], dy[j - w] + v)  # w무게를 갖는 보석만큼 빼서 빈공간 찾고 가치 더하기
print(dy[m])
        