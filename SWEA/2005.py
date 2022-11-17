t = int(input())

for tc in range(1,t+1):
    n = int(input())
    arr = [[0]*n for _ in range(n)] #계산할 배열 생성
    arr[0][0] = 1 #제일 처음 원소는 1
    for i in range(1,n): #세로
        for j in range(n): #가로
            if j == 0: #첫 원소는 1
                arr[i][j] = 1
            else: # 다음 원소는 윗 원소의 합 ,
                arr[i][j] = arr[i-1][j] + arr[i-1][j-1]
    print('#{}'.format(tc))
    for k in range(n):
        for l in range(n):
            if arr[k][l]:
                print(arr[k][l], end=' ')
        print()


