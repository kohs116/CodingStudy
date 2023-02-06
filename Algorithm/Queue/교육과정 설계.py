# 큐가 비어있어야 제대로 설계된 수업

from collections import deque

need = input()  # 필수과목의 순서
n = int(input())  # n개의 수업설계
for i in range(n):
    plan = input()
    dq = deque(need)
    for x in plan:
        if x in dq:  # 필수과목을 계획에 넣었다면
            if x != dq.popleft():  # 제일 앞 과목과 일치하지 않는다면
                print("#%d NO" % (i + 1))
                break
    else:  # 순서가 통과되었다면
        if len(dq) == 0:  # dq가 비었다면 (필수과목이 모두 들어갔다면)
            print("#%d YES" % (i + 1))
        else:
            print("%d NO" % (i + 1))
