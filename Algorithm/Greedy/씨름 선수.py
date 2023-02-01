# 키 큰 순으로 정렬하면 제일 첫번째 사람은 무조건 count
# 이후 몸무게만 판별, 키로는 못 이기기 때문
# 첫번째 사람 몸무게를 largest로 설정 해 놓고 이후 다른 사람들 몸무게와 largest 값 판별
# 더 많이 나가는 사람 있으면 largest 갱신

n = int(input())
body = []
for i in range(n):
    a, b = map(int, input().split())
    body.append((a, b))
body.sort(reverse=True)
largest = 0
cnt = 0
for x, y in body:  # x는 키, y는 몸무게
    if y > largest:
        largest = y  # 최대값 갱신
        cnt += 1
print(cnt)
