t = int(input())
for tc in range(1, t + 1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)] #퍼즐 입력 받기
    cnt = 0
    result = 0
    for i in range(n):
        for j in range(n): #가로 방향
            if arr[i][j] == 1: #단어가 들어갈 수 있는 자리
                cnt += 1
            if arr[i][j] == 0 or j == n - 1: #단어가 들어갈 수 없거나 마지막 원소일 때
                if k == cnt: # 단어의 길이와 들어갈 수 있는 자리가 같으면
                    result += 1
                cnt = 0

        for j in range(n): #세로 방향
            if arr[j][i] == 1:
                cnt += 1
            if arr[j][i] == 0 or j == n - 1:
                if k == cnt:
                    result += 1
                cnt = 0
    print('#{} {}'.format(tc, result))
