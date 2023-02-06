# import sys
# sys.stdin = open("input.txt", "rt")
n = int(input())
res = 0 # 가장 많은 상금을 받는 사람의 상금
for i in range(n):
    tmp = input().split()
    tmp.sort() # 오름차순 정렬
    a, b, c = map(int, tmp) # int 변환
    if a == b and b == c: # 같은 눈 3개
        money = 10000 + (a * 1000)
    elif a==b or a==c : # 같은 눈 2개
        money = 1000 + (a * 100)
    elif b==c : # 같은 눈 2개
        money = 1000 + (b*100)
    else: # 모두 다른 눈
        money = c * 100
    if money > res :
        res = money
print(res)