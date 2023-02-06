n = int(input())
a = list(map(int,input().split()))

avg = round(sum(a)/n)
# round는 round_half_even 방식을 택한다. 짝수 값 근사

min = 2147000000

for idx,x in enumerate(a):
    tmp = abs(x-avg) # tmp = 평균 - 현재점수
    if tmp < min : # tmp가 최소값보다도 작다면
        min = tmp # 현재 평균에 가장 가까운 점수를 min 대입
        score = x # 현재 점수
        res = idx + 1 # 현재 점수를 가지고 있는 학생 번호
    elif tmp == min :
        if x > score :
            score = x
            res = idx + 1
print(avg , res)