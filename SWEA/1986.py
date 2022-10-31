# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(T):
    t = int(input())
    res = 0
    for i in range(1, t + 1):
        if i % 2 == 0:
            res -= i
        else:
            res += i
    print("#%s" % (tc + 1), end=' ')
    print(res)

