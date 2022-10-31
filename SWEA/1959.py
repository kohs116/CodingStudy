T = int(input())

for t in range(1, T+1) :
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if N>M : #N이 M보다 커도 값을 바꿔서 무조건 M이 크도록 변환
        N,M = M,N
        B,A = A,B
    max_s = 0
    for i in range(M-N+1): #M의 시작점, 반복 가능 횟수
        temp = 0
        for j in range(N):
            temp += A[j] * B[j+i] #len(B) > len(A), 가능한 값 모두 더하기

        if temp > max_s: #더한 값을 비교하여 가장 큰 값 저장
            max_s = temp

    print("#{} {}".format(t, max_s))