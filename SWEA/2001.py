T = int(input())
sum_col = 0
sum_row = 0
for tc in range(1,T+1):
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    kill = [] #잡을 파리 수 리스트
    for i in range(n-m+1): #파리채 휘두를 간격 설정 : n-m+1
        for j in range(n-m+1):
            num = 0 # 잡을 파리 수 초기화
            for k in range(m):
                for l in range(m):
                    num += arr[i+k][j+l] #00 + 01 + 10 + 11 ...
                    print(num)
            kill.append(num)
    print("#{} {}".format(tc,max(kill)))