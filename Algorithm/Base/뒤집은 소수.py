def reverse(x): # 뒤집기 함수
    res = 0
    while x > 0 :
        t = x % 10
        res += res * 10 + t
        x = x // 10
    return res
def isPrime(x):
    if x == 1:
        return False
    for i in range(2,x//2 + 1):
        if x%i == 0:
            return False
        else:
            return True

n = int(input()) # n개의 자연수
a = list(map(int,input().split())) # 자연수 리스트

for x in a :
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end = ' ')
