from collections import deque

n, m = map(int, input().split())
Q = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
# (pos,val) = (0,60) , (1,50) , (2,70) .. tuple

Q = deque(Q)
cnt = 0
while True:
    cur = Q.popleft()  # cur = (0,60) , cur[0]=0 cur[1]=60
    if any(cur[1] < x[1] for x in Q):  # 위험도 비교
        Q.append(cur)  # 현재보다 위험도 높은 사람이 존재하면 진료 X
    else:
        cnt += 1
        if cur[0] == m:
            break
print(cnt)