def DFS(L, sum):  # L=동전 개수, sum=누적 금액
    global m, res
    if L > res:  # L은 이미 최소이기 때문에 그 이상의 값은 필요 없음
        return
    if sum > m:  # 누적 금액이 거슬러 주어야 할 m보다 크다면
        return
    if sum == m:  # 누적 금액과 거슬러 주어야 할 금액이 같다면
        if L < res:  # res를 최대로 설정 해 놓았으므로 L이 무조건 작음
            res = L  # res 갱신
    else:  # 누적 금액이 아직 m만큼 차지 않았다면
        for i in range(n):  # 동전 종류 개수만큼 반복
            DFS(L + 1, sum + a[i])  # level+1, sum+동전 금액


if __name__ == "__main__":
    n = int(input())  # 동전 종류 개수
    a = list(map(int, input().split()))  # 동전 종류
    m = int(input())  # 거슬러 줄 금액
    res = 2147000000  # 최소를 출력할 거니까 2147000000
    a.sort(reverse=True)  # 내림차순 정렬해서 가장 큰 단위부터 나누기
    DFS(0, 0)
    print(res)
