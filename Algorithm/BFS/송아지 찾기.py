from collections import deque

MAX = 10000  # 좌표 맥시멈
ch = [0] * (MAX + 1)
dis = [0] * (MAX + 1)
n, m = map(int, input().split())  # 출발점, 도착점
ch[n] = 1  # 출발
dis[n] = 0
dQ = deque()
dQ.append(n)
while dQ:
    now = dQ.popleft()
    if now == m:
        break
    for next in (now - 1, now + 1, now + 5):
        if 0 < next <= MAX:
            if ch[next] == 0:  # 방문 안했을 때
                dQ.append(next)
                ch[next] = 1
                dis[next] = dis[now] + 1
print(dis[m])
