#두 개의 정 n면체와 정 m면체의 두 주사위를 던져서 나올 수 있는
# 눈의 합 중 가장 확률이 높은 숫자를 출력
# 정답이 여러개일 경우 오름차순 출력

n,m = map(int,input().split())
cnt = [0]*(n+m+3)
max = 2147000000

for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j] += 1
        ## cnt counting
for i in range(n+m+1):
    if cnt[i]>max:
        max = cnt[i]
for i in range(n+m+1):
    if cnt[i] == max:
        print(i, end=' ')