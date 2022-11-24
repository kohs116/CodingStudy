def solution(n, a, b):
    answer = 0
    while a != b:  # a=1 b=2 가 될 때 까지 반복
        answer += 1
        a, b = (a + 1) // 2, (b + 1) // 2

    return answer
