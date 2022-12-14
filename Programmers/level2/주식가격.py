from collections import deque


def solution(prices):
    queue = deque(prices)
    answer = []

    while queue:
        price = queue.popleft()
        # popleft() 하고 남은 값들 순회
        sec = 0
        for q in queue:
            sec += 1
            if price > q:
                break
        answer.append(sec)
    return answer
