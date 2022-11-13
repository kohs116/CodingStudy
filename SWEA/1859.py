# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    nli = list(map(int, input().split()))
    nli_max = nli[-1]
    answer = 0
    for i in range(n - 2, -1, -1):
        if nli_max <= nli[i]:
            nli_max = nli[i]
        else:
            answer += nli_max - nli[i]
    print('#{} {}'.format(tc, answer))





