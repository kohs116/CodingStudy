from collections import deque

n, k = map(int, input().split())
dq = list(range(1,n+1))
dq = deque(dq)
while dq: #큐가 비게 되면 멈춤
    for _ in range(k-1):
        cur = dq.popleft()
        dq.append(cur)
    dq.popleft()

    if len(dq) == 1:
        print(dq[0])
        dq.popleft()



