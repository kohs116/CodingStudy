def solution(n):
    # 피보나치 수열 활용
    if n == 1:
        return 1
    else:
        dp = [0] * (n + 1)

        dp[1] = 1
        dp[2] = 2
        # d1[1]과 dp[2]는 각각 1,2로 값 고정

        for i in range(3, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567

    return dp[-1]
    # 가장 마지막 값 반환
