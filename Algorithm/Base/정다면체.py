n,m = map(int,input().split()) # 정 n면체와 정 m면체 입력
cnt = [0]*(n+m+3) # 두 주사위 눈의 합은 총 n*m개의 결과를 가지므로 넉넉하게 +3
max = 2147000000

for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j] += 1 # 0~(n*m) 인덱스에 카운팅 될 때마다 +1
for i in range(n+m+1):
    if cnt[i]>max: # 카운팅 된 숫자가 최대값보다 크다면
        max = cnt[i]
for i in range(n+m+1):
    if cnt[i] == max:
        print(i, end=' ')