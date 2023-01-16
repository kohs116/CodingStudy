n = int(input())
a = list(map(int,input().split()))

avg = round(sum(a)/n)
# round는 round_half_even 방식을 택한다. 짝수 값 근사

min = 2147000000

for idx,x in enumerate(a):
    tmp = abs(x-avg)
    if tmp < min :
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min :
        if x > score :
            score = x
            res = idx + 1
print(avg , res)