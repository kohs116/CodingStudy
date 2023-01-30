# 격자판에서 행(h),0/1(t),회전 수(k) 가 주어지면 모래시계 모양의 최종 감의 개수 출력

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
for i in range(m):  # 회전 처리
    h, t, k = map(int, input().split())
    if t == 0:
        for _ in range(k):
            a[h - 1].append(a[h - 1].pop(0))  # 실제 인덱스와 입력 인덱스 차이 1
    else:
        for _ in range(k):
            a[h - 1].insert(0, a[h - 1].pop())  # 제일 뒤 값을 꺼냄
res = 0
s = 0
e = n - 1
for i in range(n):
    for j in range(s, e + 1):
        res += a[i][j]  # 0~4
    if i < n // 2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(res)
