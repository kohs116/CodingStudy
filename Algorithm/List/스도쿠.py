# 스도쿠 정확하게 풀었으면 YES 아니면 NO 출력
# 행과 열, 3*3 보드에 숫자 중복없이 나타나도록
# 리스트를 만들어서 숫자마다 count후 총 합이 9이면 YES 아니면 NO
def check(b):
    for i in range(9):
        ch1 = [0] * 10  # 행 체크
        ch2 = [0] * 10  # 열 체크
        for j in range(9):
            ch1[a[i][j]] = 1 #누적합 X
            ch2[a[i][j]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9:
            return False
    for i in range(3):
        for j in range(3):  # 그룹
            ch3 = [0] * 10
            for k in range(3):
                for s in range(3):  # 값
                    ch3[a[i * 3 + k][j * 3 + s]] = 1
            if sum(ch3) != 9:
                return False
    return True


a = [list(map(int, input().split())) for _ in range(9)]
if check(a):
    print("YES")
else:
    print("NO")