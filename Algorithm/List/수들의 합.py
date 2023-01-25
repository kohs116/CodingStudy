# n개의 수로 된 수열이 있다. 이 수열의 i~j까지 수의 합이 m이 되는 경우의 수
# 연속적인 부분수열의 합 = m

# tot = lt~rt까지의 합 (rt바로 앞 값 까지, rt는 해당 X)
# 부분수열의 합이 m보다 <작으면 rt+1>, <같으면 cnt+1 하고 lt+1>, <크면 lt+1>
# rt가 마지막까지 처리하고 n에 있으면 break

n, m = map(int, input().split())
a = list(map(int, input().split()))
lt = 0
rt = 1
tot = a[0] #제일 첫번째 값부터 더하기
cnt = 0

while True:
    if tot < m:
        if rt < n:
            tot += a[rt]
            rt += 1
        else: # rt가 n까지 도달하면 break
            break
    elif tot == m:
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1

print(cnt)
