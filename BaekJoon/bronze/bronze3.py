""" #1085 직사각형에서 탈출
x, y, w, h = map(int,input().split())
print(min(x,y,w-x,h-y))
#x와 y를 min에 넣은 이유는 (w,h)보다 x축 or y축에 접할 때가 더 가까울 수 있으므로
"""

""" #1247 부호
#3 입력하면 데이터 3개 입력 / 10 입력하면 데이터 10개 입력 ...
#위 과정을 세번 반복

import sys
for _ in range(3):
    n = int(sys.stdin.readline())
    data = [int(sys.stdin.readline()) for i in range(n)]
    if sum(data)==0:
        print("0")
    elif sum(data)>0:
        print("+")
    else: print("-") """

""" #1267 핸드폰 요금
#영식- (n//30)*10 + 10
#민식- (n//60)*15 + 15
n = int(input()) #통화 개수
a = list(map(int,input().split())) #통화 개수 만큼 입력되어 있음
y=m=0

for i in a:
    y+=(i//30)*10 + 10
    m+=(i//60)*15 + 15

if y==m:
    print("Y M",m)
elif y>m:
    print("M",m)
else: print("Y",y) """

""" #1284 집 주소
while 1:
    n = input()
    if n=='0':
        break #0 입력 시 입력종료
    l=len(n)+1 # 호수판 길이 l
    for i in n : #n의 문자 하나하나씩 검토
        if i=='0':
            l+=4
        elif i=='1':
            l+=2
        else: l+=3
    print(l) #최종 합산 출력 """

""" #1547 공
c = [0,1,0,0] #컵 3개 list
m = int(input()) #위치 바꾼 횟수 m
for i in range(m):
    x, y = map(int,input().split())
    c[x], c[y] = c[y], c[x] #입력된 x,y를 통해 컵 위치 변경
for i in range(4): #0~3까지의 인덱스에서 1을 가지는 값 확인 후 출력
    if c[i]==1:print(i) """

""" #2438 별 찍기-1
n = int(input())
for i in range(1,n+1):
    print("*"*i) """

""" #2439 별 찍기-2
n = int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)
#만약 n=3 이면 3-1 3-2 3-3 만큼의 공백 출력 후 * 출력 """

""" #2443 별 찍기-6
n=int(input())
for i in range(n,0,-1):
    print(" "*(n-i) + "*"*((2*i)-1)) """

""" #2444 별 찍기-7
n=int(input())
for i in range(1,n):
    print(" "*(n-i)+"*"*((2*i)-1))
for j in range(n,0,-1):
    print(" "*(n-j) + "*"*((2*j)-1)) """

""" #10872 팩토리얼
#알고리즘
#만약 n입력받으면 n*(n-1)*(n-2)*...*(n-(n-1))
n = int(input())
a=1
for i in range(0,n):
    a *= n-i
print(a) """

""" #2576 홀수
li=[] #홀수 넣어줄 리스트 생성
for i in range(7):
    n = int(input()) #자연수 7개 입력받음
    if n%2!=0: # n 중 홀수가 있다면
        li.append(n) #li 리스트에 홀수값을 넣어줌

if len(li)==0: #li에 값이 없다면
    print(-1) #-1 출력
else:
    print(sum(li))
    print(min(li)) """

""" #10818 최소,최대
import sys
n = sys.stdin.readline()
a = list(map(int,sys.stdin.readline().split()))
print(min(a), max(a)) """



