T = int(input())
for tc in range(1, T + 1):
    tc = str(tc)
    answer = tc.count('3') + tc.count('6') + tc.count('9')
    if answer == 0:
        print(tc, end=' ')
    else:
        print("-" * answer, end=' ')