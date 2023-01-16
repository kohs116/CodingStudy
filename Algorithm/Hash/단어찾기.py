n = int(input())
p = dict()
for i in range(n):
    word = input()
    p[word] = 1
for i in range(n-1): #실제 시에 쓰인 단어
    word = input()
    p[word] = 0 #시에 쓰인 단어는 0으로 바꿈
for key,value in p.items():
    if value == 1:
        print(key)
        break