def solution(N):
    answer = 0
    while N > 0:
        answer += N % 2  # *2만큼 순간이동 가능하므로 2로 나눈 나머지는 더해줌
        N //= 2  # 순간이동
    return answer
