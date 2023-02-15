def DFS(L, sum):  # L 인덱스 , sum 무게
    global res
    if L == n:
        if 0 < sum <= s:  # 대칭구조로 나타나기 때문에 음수는 판별할 필요 없음
            res.add(sum)  # append 불가

    else:
        DFS(L + 1, sum + G[L])  # 왼쪽에 추 넣기
        DFS(L + 1, sum - G[L])  # 오른쪽에 추 넣기
        DFS(L + 1, sum)  # L번째 추를 사용하지 않겠다는 의미


if __name__ == "__main__":
    n = int(input())
    G = list(map(int, input().split()))
    s = sum(G)
    res = set()  # 중복 제거하면서 값 추가
    # set()에 넣는 이유 - 1g 측정값이라도 경우의 수가 여러가지가 나올 수 있기 때문에 중복제거 가능한 set() 사용
    DFS(0, 0)
    print(s - len(res))
