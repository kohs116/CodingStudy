
#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    answer = 0
    li = list(map(int,input().split()))
    li.sort()
    for i in range(1,len(li)-1):
        answer += li[i]
    result = answer/8
    print("#{} {}".format(tc,round(result)))

