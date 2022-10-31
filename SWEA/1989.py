# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    s = input()
    sr = s[::-1]
    if (s == sr):
        print("#%s" % tc, end=' ')
        print(1)
    else:
        print("#%s" % tc, end=' ')
        print(0)
