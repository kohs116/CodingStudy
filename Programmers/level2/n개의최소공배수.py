def solution(arr):
    from math import gcd  # 최대공약수 gcd()
    answer = arr[0]
    for i in arr:  # 모두 곱한 값을 최대공약수로 나누고 저장
        answer = answer * i // gcd(answer, i)

    return answer
