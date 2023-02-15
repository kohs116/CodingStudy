def DFS(L):
    global res
    if L == n:
        minus = max(money) - min(money)
        if minus < res:
            tmp = set()
            for x in money:
                tmp.add(x)
            if len(tmp) == 3:  # 중복 제거 했는데도 여전히 길이가 3이면 res 갱신
                res = minus
    else:
        for i in range(3):  # 세명
            money[i] += coin[L]
            DFS(L + 1)
            money[i] -= coin[L]  # back


if __name__ == "__main__":
    n = int(input())  # 동전 개수
    coin = []
    money = [0] * 3  # 각 사람의 금액 담을 리스트
    for _ in range(n):
        c = int(input())
        coin.append(c)
    res = 2147000000
    DFS(0)
    print(res)
