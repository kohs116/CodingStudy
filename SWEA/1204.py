# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
m = 0
for tc in range(1, T + 1):
    num = int(input())
    num_li = list(map(int, input().split()))
    for i in range(len(num_li)):
        if num_li.count(i) == 0:
            continue
        elif num_li.count(i) >= num_li.count(m):
            m = i
    print("#{} {}".format(tc,m))



