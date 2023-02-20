n = int(input())
coin = list(map(int, input().split()))
m = int(input())
dy = [1000] * (m + 1)  # 최소를 구할거니까 최대값으로 설정
dy[0] = 0  # 0원을 거슬러주는 방법의 개수는 0
for i in range(n):
    for j in range(coin[i], m + 1):
        dy[j] = min(dy[j], dy[j - coin[i]] + 1)
print(dy[m])