# 제일 가벼운사람과 제일 무거운사람을 짝지어 m보다 큰 지 작은 지 판별
"""
n, limit = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
cnt = 0
while p:
    if len(p) == 1:  # 한명 남았을 때
        cnt += 1
        break
    if p[0] + p[-1] > limit:  # 제일 가벼운사람 + 제일 무거운사람
        p.pop()  # 제일 무거운 사람만 탈출
        cnt += 1
    else:
        p.pop(0)  # 제일 가벼운 사람 +
        p.pop()  # 제일 무거운 사람 두명 탈출
        cnt += 1
print(cnt)

"""
from collections import deque
n, limit = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
p=deque(p)
cnt = 0
while p:
    if len(p) == 1:  # 한명 남았을 때
        cnt += 1
        break
    if p[0] + p[-1] > limit:  # 제일 가벼운사람 + 제일 무거운사람
        p.pop()  # 제일 무거운 사람만 탈출
        cnt += 1
    else:
        p.popleft()  # 제일 가벼운 사람 +
        p.pop()  # 제일 무거운 사람 두명 탈출
        cnt += 1
print(cnt)
