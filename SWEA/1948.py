# 1. dict에 1월~12월 일자 넣기
# 2. fm fd lm ld 입력받기
# 3. fm==lm 이면 ld-fd 출력
# 4. fd+
# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
dict = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for tc in range(1, T + 1):
    fm, fd, lm, ld = map(int, input().split())
    if fm == lm:
        print("#%d" % tc, end=' ')
        print(ld - fd + 1)
    else:
        f = dict[fm] - fd + ld + 1  # 26+31이 아니라 15여야함 = 41
        for i in range(1, lm - fm):  # 1,2
            f += dict[fm + i]  # 41+30+31 = 102
        print("#%d" % tc, end=' ')
        print(f)


