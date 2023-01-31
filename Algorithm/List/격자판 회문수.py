board = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
for i in range(3):  # 0~4, 1~5, 2~6 7이상의 인덱스는 없기 때문
    for j in range(7):  # 행
        tmp = board[j][i:i + 5]  # 0~4, 1~5, 2~6 분리 위해 i:i+5
        if tmp == tmp[::-1]:  # 회문 판별
            cnt += 1
        for k in range(2):  # 세로
            if board[i + k][j] != board[i + 5 - k - 1][j]:  # 0행-4행 1행-3행 .. 비교
                break
        else:
            cnt += 1
print(cnt)
