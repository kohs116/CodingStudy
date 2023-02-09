L = int(input()) # 창고 가로의 길이
a = list(map(int, input().split())) # 높이 리스트
m = int(input()) # 조정 횟수
a.sort()
for _ in range(m): # m회 조정
    a[0] += 1
    a[L - 1] -= 1
    a.sort()
print(a[L - 1] - a[0])
