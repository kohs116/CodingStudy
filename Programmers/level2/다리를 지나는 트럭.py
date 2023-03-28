def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = [0] * bridge_length  # 빈자리 0으로 메꾸기

    while q:
        q.pop(0)
        answer += 1
        if truck_weights:
            if sum(q) + truck_weights[0] <= weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)

    return answer