# 입력을 넣을 때 부호를 바꿔 넣기 (최소힙과 반대)
import heapq as hq  # heapq는 기본적으로 최소힙

a = []
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(-hq.heappop(a))
    else:
        hq.heappush(a, -n)
