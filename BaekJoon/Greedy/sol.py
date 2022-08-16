"""
#설탕 배달
#n이 5의 배수가 아니라면 5의배수가 될 때 까지 3만큼 빼주기
n = int(input()) #n kg
result = 0

while n>=0:
    if n %5 ==0 : #n이 5의 배수라면
        result += n//5 #5로 나눈 몫을 result에 저장
        print(result)
        break
    n -= 3 #n이 5의 배수가 아니라면 n에서 3만큼 빼기
    result += 1 #차감 후 result에 +1 , 이 과정을 5의 배수가 될 때 까지 반복
else: #while문이 거짓일 경우
    print(-1) """
import heapq

""" #ATM
#주어진 숫자의 누적 합을 구하는 문제
#누적 합 구할 배열 result
n = int(input()) #n명의 사람들
s = list(map(int,input().split())) #각 사람이 돈 인출하는데 필요한 시간
s.sort() #시간 합 최솟값 구하기 위해 정렬
result = 0
for i in range(n):
    for j in range(i+1):
        result += s[j]
        #s[0]+s[1]+... s[i] 과정을 n번 반복
print(result)
"""

""" #동전 0
#n개의 동전으로 k원을 만들어야함 , 동전 개수를 최소로
#1.입력된 n개의 동전 for reversed 2. 앞의 값 부터 나머지 있는 지 판별
#3.몫은 result에 저장하고 나누고 난 나머지는 r에 저장
#4.r을 다시 나눈 몫을 result에 저장, 그 나머지 다시 r에 저장
n, k = map(int,(input().split())) #n개의 동전, k원
num=list()
result = 0
r = 0
for nu in range(n):
    num.append(int(input()))

for i in reversed(range(n)):
    if k>=num[i]:
        result += k // num[i]
        k = k%num[i]
    else: continue

print(result) """

""" #회의실 배정
#n개의 회의 각 회의 i 가 안 겹치게 회의실 사용할 수 있는 최대 개수
#s 먼저 정렬하고 f기준 오름차순 다시 정렬해야함
n = int(input()) # 회의의 수
li=list()
count = 0
for i in range(n):
    s,f = map(int,input().split())
    li.append([s,f])

li = sorted(li,key=lambda x:x[0]) #s 기준 정렬
li = sorted(li,key=lambda x:x[1]) #f 기준 정렬

last=0
for i,j in li:
    if i >= last:
        count +=1
        last = j

print(count) """

""" #보물
# 0 1 1 1 6
# 8 7 3 2 1
# 7+3+2+6 = 18
# a는 오름차순 정렬, b는 내림차순 정렬
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
result = 0
a.sort()
b.sort(reverse=True)
for i in range(n):
    result += (a[i]*b[i])

print(result) 

"""

""" #잃어버린 괄호
#앞에 + 부호가 오면 괄호 크게 의미 없음
#앞에 - 부호가 오면 뒤에를 괄호로 묶어야함
#55-(50+40)

s = input().split('-') #-부호 기준으로 문자열 자름
c=0 # 최종 결과값
for i in s[0].split('+'): #s[0]=맨 앞 문자부터 - 부호 나오기 전 까지의 문자열 / s[0]을 다시 + 부호로 split
    c += int(i) #split한 문자열을 int형으로 변환 후 더해주기
for j in s[1:]: #이후 문자열부터
    for k in j.split('+'): #+부호로 split
        c -= int(k) #괄호 계산 위해 +부호가 붙은 값에는 -부호 달아서 빼주기
print(c)
"""

""" #거스름돈
#1000-n -> 결과 값을 500,100,50,10,5,1 순으로 나누기
n = 1000-int(input())
c = [500,100,50,10,5,1]
count = 0
for i in c:
    count += n//i #나눈 몫 만큼 count에 +
    n%=i #n에 나머지 저장
print(count) """

""" #로프
#최소중량 로프 X 연결 로프 수 의 최대값
n = int(input())
a=list()
ans=list()
for i in range(n):
    a.append(int(input()))
a.sort(reverse=True) #오름차순 정렬

for i in range(n):
    ans.append(a[i]*(i+1))
print(max(ans))
"""

""" #주유소
#제일 왼쪽 리터당 가격 X 제일 왼쪽 이동거리
#두번째 부터 리터당 가격이 제일 작은 값 찾아야함
#찾기 전까지는 두번째부터 리터강가격 X 이동거리 계산해서 더해야함

n = int(input()) #도시의 개수
c = list(map(int,input().split())) #도로의 길이
l = list(map(int,input().split())) #리터당 가격
r1 = c[0]*l[0] #첫번째 값 고정
mc = l[0] #리터당 가격 최소인 지점 고정

for i in range(1,n-1): #1~n-2
    if mc>l[i]: #고정되어있던 최소 지점 판별
        mc = l[i] #최소 지점 바뀌어 저장
    r1 += (mc * c[i]) #첫번째값에 이후 계산된 값 더하기

print(r1) """

""" #수들의 합
#1부터 n까지의 합이 s, n의 최댓값
#쭉 더해서 합이 s보다 커지면 반복문 멈추고 출력
s = int(input())
n=1
while n*(n+1)/2 <=s: #n까지의 합 공식이 입력된 s보다 작다면 출력하지 않고 n+1
    n+=1
print(n-1) #while문 탈출 후 s를 넘으면 안되므로 n-1
"""

""" #30
#배수판정법- 각 자리의 수 합이 3의 배수이어야 하고 끝자리가 0이어야함
n = list(input())
n.sort(reverse=True) #입력받은 n을 내림차순 정렬
sum=0
for i in n:
    sum+=int(i) #n의 각 자리 수 합을 sum에 저장
if sum%3!=0 or "0" not in n: #각 자리의 수 합이 3의 배수가 아니거나 0이 포함되어 있지 않다면
    print(-1) #-1 출력
else: print("".join(n)) # 그렇지 않다면 조건 충족하는 n 출력
"""

""" #신입 사원
#테스트케이스 t, 지원자 수 n, t개의 세트에 n줄만큼 입력
#서류를 내림차순 정렬 후 면접 순위 판별
#순위를 판별하므로 숫자가 작을수록 선발 유리
#서류순위 내림차순 정렬 후 [0][1]을 max로 설정하고 값 바꿔가면서 판별
import sys
t = int(sys.stdin.readline()) #테스트케이스
for i in range(t):
    l = list()  # 입력받을 리스트 생성
    n = int(sys.stdin.readline())
    for j in range(n):
        l.append(list(map(int,sys.stdin.readline().split())))
    l.sort() #정렬
    max = l[0][1]
    count = 1

    for k in range(1,n):
        if max>l[k][1]: # [0][1] > [1][1] ...~~
            count+=1
            max = l[k][1]
    print(count)
    """

# 카드 정렬하기
# 누적 합
""" n = int(input())
card = []
for i in range(n):
    card.append(int(input()))
card.sort()
result=0
for j in range(len(card)-1): #0,1,2,3
    result += card[j]+card[j+1] #0/1 1/2 2/3
    card[j+1]=result
print(result) 
-> 메모리초과로 힙 알고리즘 이용
-> 힙 알고리즘은 부모노드의 두 자식노드 중 크기가 더 큰 자식을 부모와 바꾸는 알고리즘
-> 자식이 더이상 존재하지 않을 때 까지 반복
"""
""" import sys
import heapq #힙 사용
n = int(sys.stdin.readline())
card = []
for i in range(n):
    heapq.heappush(card,int(sys.stdin.readline())) #힙에 원소 추가
if len(card) == 1: #비교할 값이 없으면
    print(0) #0출력
else:
    result = 0 #비교 횟수
    while len(card) > 1:
        card1 = heapq.heappop(card) #제일 작은 값
        card2 = heapq.heappop(card) #card1 다음으로 작은 값
        result += card1 + card2 #값 더해줌
        heapq.heappush(card,card1+card2) #더한 값 다시 넣어줌
print(result)

#30+40 + 30+40+50 + 30+40+50+100 = 70+120+220= 410
"""

# 단어 수학
# 자릿수대로 가장 큰 숫자 대입
"""
import sys
n=int(sys.stdin.readline())
s=[]
s_dict = {} # value:10000,1000,100,10,1
num = [] #s_dict 수 저장

for i in range(n):
    s.append(sys.stdin.readline().rstrip())
for i in range(n):
    for j in range(len(s[i])):
        if s[i][j] in s_dict:
            s_dict[s[i][j]] += 10 ** (len(s[i])-j-1)
        else:
            s_dict[s[i][j]] = 10 ** (len(s[i])-j-1)
        # 알파벳별로 각 자리수 판별 (a**b = a^b)

for val in s_dict.values(): #value값 num에 저장
    num.append(val)
num.sort(reverse=True) #저장된 값 내림차순 정렬
sum=0 #출력할 값
pows=9 #0~9
for i in num:
    sum+=pows*i
    pows-=1 #i와 곱해주고 난 뒤 -1
print(sum)
"""

# 뒤집기
# 문자열에서 저장되어있는 문자와 다른 문자가 나오면 count+1
""" s=input()
count=0
prev='?' # 0/1 뭐로 시작하든 상관없음
for i in s: #입력받은 문자열의 문자 검사
    if i !=prev: #저장되어 있는 문자와 다른 문자가 나온다면
        prev=i #문자를 prev에 저장
        count+=1
print((count)//2) #문자가 변할때마다 count에 +1 하여 2로 나눈 몫 출력
"""

# A→B
# B→A 로 생각하기, 숫자에 1이 붙어있으면 지우고, 이후 짝수면 2로 나누기
""" a,b = map(int,input().split())
count=1 #연산 횟수
while True:
    if b==a:
        break
    elif (b%2!=0 and b%10!=1) or (b<a): #b가 2로 나누어 떨어지지 않고 끝자리가 1이 아니거나 b가 a보다 크다면
        count=-1 #-1 출력
        break
    else:
        if b%10==1: #b의 끝자리가 1이면
            b//=10 #1 지우고
            count+=1 #횟수에 +1
        else:
            b//=2 #2로 나누어 떨어진다면
            count+=1 #횟수에 +1

print(count)
"""

# 캠핑
# l=5 p=8 v=20
# 연속하는 8일 중 5일동안만 사용 가능, 이제 막 20일짜리 휴가 시작
# 처음 5일 쓰고 3일 못하고 또 5일 쓰고 ... 반복
# 1~5 사용 6~8 쉬고 9~13 사용 14~16 쉬고 17~20 쓰고
# 총 14일 사용 가능
# v%p가 l보다 크다면? l을 더해주어아 함
# v//p = 2. 2 * l = 10. 10+v%p(=4) = 14
""" i=1 #첫번째 줄은 case1
while True:
    l, p, v = map(int, input().split())
    if l==0 and p==0 and v==0:
        break
    else:
        vp1 = v//p
        vp2 = v%p
        if v%p > l:
            print("Case %d: %d"%(i,vp1*l + l))
        else:
            print("Case %d: %d"%(i,vp1*l + vp2))
        i+=1 #다음 케이스 출력위해 +1
"""

# 보석 도둑
# 보석 총 n개 각 보석은 무게 m 가격 v 가지고있음.
# 가방 k개 가지고 있고 최대 c무게 까지 담을 수 있음. 가방엔 한개 보석만 넣을 수 있음.
# 훔칠 수 있는 보석의 최대 가격은?

# 보석 3개, 가방 2개
# m=1,5,2 v=65,23,99
# 가방엔 각각 10,2 까지 담을 수 있음
# 99+65 = 164
# 우선순위 큐
"""
import heapq
import sys
n,k = map(int,sys.stdin.readline().split())
nk_li = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
c_li = [int(sys.stdin.readline()) for _ in range(k)]
nk_li.sort()
c_li.sort()

q=[]
result=0

for i in c_li: #가방이 담을 수 있는 무게 i
    while nk_li and nk_li[0][0] <= i:
    # 가방에 담을 수 있는 최대 무게 c보다 보석 무게가 같거나 작은 경우
        heapq.heappush(q,-heapq.heappop(nk_li)[1])
        #큐에 가장 높은 금액을 넣어줌 (최대힙)
    if q:
        result -= heapq.heappop(q) #결과값에 더해주기 위해 다시 -부호 붙임
print(result)
"""

# 기타줄
# 끊어진 기타줄 n개, 기타줄 브랜드 m개
# 각 브랜드의 패키지 , 낱개 가격이 공백으로 구분
"""
n,m = map(int,input().split())
pack = list()
item = list()

for j in range(m):
    p,i = map(int,input().split())
    pack.append(int(p)) #패키지 가격을 pack 리스트에 넣음
    item.append(int(i)) #낱개 가격을 item 리스트에 넣음

minp = min(pack) #패키지 가격중 가장 저렴한 가격을 minp 라고 정의
mini = min(item) #낱개 가격중 가장 저렴한 가격을 mini 라고 정의

if minp<mini*6: #패키지 가격이 낱개*6 한 값보다 저렴하고
    if minp < (n%6)*mini:
    #(패키지는 6개입이므로)n을 6으로 나눈 나머지에 낱개가격을 곱한 값이 제일 저렴한 패키지 가격보다 비싸다면
        print((n//6)*minp + minp) #6으로 나눈 몫과 나머지 모두 패키지 값으로 계산
    else: #n을 6으로 나눈 나머지에 낱개가격을 곱한 값이 제일 저렴한 패키지 가격보다 저렴하다면
        print((n//6)*minp + (n%6)*mini)
        #몫에는 패키지가격, 나머지에는 낱개가격 계산
elif minp >= mini*6 : #패키지가격이 낱개*6 한 값보다 비싸다면
    print(n*mini) #낱개가격으로 계산
"""

# 수 묶기
# 음수, 양수, 1 일 경우의 케이스를 각각 나누어 계산
"""
n = int(input()) #수열의 크기 n
minus_list=[] #음수 리스트
plus_list=[] #양수 리스트
one_list=[] #숫자 1 리스트
ans=0 #출력

for i in range(n):
    num=int(input())
    if num>1:
        plus_list.append(num)
    elif num<=0:
        minus_list.append(num)
    else:
        one_list.append(num)
plus_list.sort(reverse=True) #내림차순 정렬
minus_list.sort() #오름차순 정렬

if len(plus_list) % 2 == 1: #양수 개수가 홀수면
    ans+= plus_list[len(plus_list)-1] #제일 작은 값 ans에 더하기
    for j in range(0,len(plus_list)-1,2): #step=2
        ans+=plus_list[j]*plus_list[j+1] #나머지 값들은 곱해서 더하기
else:
    for j in range(0,len(plus_list),2): #양수 개수가 짝수면
        ans+= plus_list[j] * plus_list[j+1] # 다 곱해서 더하기

if len(minus_list) % 2 == 1: #음수 개수가 홀수면
    ans+= minus_list[len(minus_list)-1] #제일 작은 값 ans에 더하기
    for j in range(0,len(minus_list)-1,2): #step=2
        ans+= (minus_list[j]) * (minus_list[j+1]) #나머지 값들은 곱해서 더하기
else:
    for j in range(0,len(minus_list),2): #음수 개수가 짝수면
        ans+= minus_list[j] * minus_list[j+1] #다 곱해서 더하기

for j in range(len(one_list)):
    ans+= one_list[j] #1은 더해주기

print(ans)
"""

# 5와 6의 차이
# 5일때 최소 6일때 최대
# replace 함수 사용 : 어떤 값 찾아 바꿔줌
"""
a, b = map(str,input().split())
min = int(a.replace('6','5')) + int(b.replace('6','5'))
#최소값은 a or b의 문자열에서 6을 5로 바꿈
max = int(a.replace('5','6')) + int(b.replace('5','6'))
#최대값은 a or b의 문자열에서 5를 6으로 바꿈
print(min,max)
"""

# 문서 검색
# 입력한 문자열에 특정 문자열이 몇번 포함되어 있는 지?
"""
d=input() #문서
f=input() #검색 단어

if f in d:
    print(d.count(f))
else:
    print("0")
"""

# 수리공 항승
# 반복 시작지점 start 중요
"""
n, l = map(int,input().split())
nli=list(map(int,input().split()))
nli.sort()
c=1
start=nli[0]-0.5

for i in range(len(nli)):
    if start+l >= nli[i]+0.5:
        continue
    else:
        c+=1
        start = nli[i]-0.5

print(c)
"""

# 행렬
# 3X3 크기의 부분행렬 뒤집어 연산
# 1행-2행 1열-2열 이동하고 (1,1)이 동일하는 지 확인
"""
n, m = map(int,input().split())
a=[list(map(int,input().rstrip()))for i in range(n)]
b=[list(map(int,input().rstrip()))for j in range(n)]
c=0

def flip(i,j):
    for x in range(i,i+3):
        for y in range(j,j+3): # 3X3 부분행렬
            a[x][y] = 1 - a[x][y]
            # 1이면 0으로, 0이면 1로 바꿈
for i in range(n-2):
    for j in range(m-2): # 1행에서 2행까지, 1열에서 2열까지
        if a[i][j] != b[i][j]:
            flip(i,j)
            c+=1
        if a==b:
            break
    if a==b:
        break
if a!=b:
    print(-1)
else: print(c)
"""

# 저울
# 가능한 합의 결과들을 나열하고 최대값 +1
"""
n = int(input())
nli=list(map(int,input().split()))
nli.sort()
c=1 #빈공간 출력 위해 1로 초기화
for i in nli:
    if c<i: #nli의 작은값부터 판별
        break
    c+=i #c가 i보다 크다면 계속 더하기

print(c)
"""

# 강의실 배정
# 우선순위 큐
"""
import sys
import heapq
q=[] #큐 생성
n = int(sys.stdin.readline())
for i in range(n):
    s, t = map(int,sys.stdin.readline().split())
    q.append([s,t]) #q에 입력받은 s,t 넣음
q.sort() #시작시간 기준 정렬
nli=[] #새로운 큐 생성
heapq.heappush(nli,q[0][1])
#첫번째 회의 끝나는 시간을 nli에 넣어줌

for i in range(1,n):
    if q[i][0] < nli[0]: #nli[0]=q[0][1]
    #현재 회의 끝나는 시간보다 다음 회의 시작시간이 더 빠르면
        heapq.heappush(nli,q[i][1])
        #nli에 다음 회의 시작시간 넣어줌
    else: #현재 회의실 그대로 진행 가능하면
        heapq.heappop(nli)
        #그 다음 회의 시간 변경위해 pop
        heapq.heappush(nli,q[i][1])
        #그 다음 회의 끝나는 시간 넣어줌
print(len(nli))
"""

# 세탁소 사장 동혁 / 거스름돈 문제
# q=0.25 d=0.10 n=0.05 p=0.01
"""
t = int(input())
tli=list()

for i in range(t):
    tli.append(int(input()))

for i in range(t):
    if tli[i] % 25 == 0:
        q= tli[i] // 25
        d=0
        n=0
        p=0
    else:
        q= tli[i] // 25
        r = tli[i] % 25
        if r % 10 == 0:
            d= r // 10
            n=0
            p=0
        else:
            d= r // 10
            r = r % 10
            if r % 5 == 0:
                n=r // 5
                p=0
            else:
                n = r //5
                r = r % 5
                p = r
    print(q,d,n,p)
"""

# 병든 나이트
# f=(2,1) s=(1,2) t=(-1,2) fo=(-2,1)
# 바둑판
"""
n,m = map(int,input().split())
if n==1:
    print(1)
elif n==2:
    #n==2이면 s,t만 사용가능하고 최대 4번까지, 4번보다 작다면 (m+1)//2
    print(min(4,(m+1)//2))
elif n > 2 and m < 7:
    #이동 횟수가 4번 이하
    print(min(4,m))
else: #이동 횟수 4번 이상
    print(m-2)
"""

# 멀티탭 스케줄링
"""
n,k = map(int,input().split())
kli=list(map(int,input().split()))
c=0
pli=list()
for i in range(k):
    if kli[i] in pli:
        continue
    #1.이미 꽂혀있을 때
    if len(pli) != n:
        pli.append(kli[i]) #빈공간에 현재 플러그 꽂아줌
        continue
    #2.멀티탭에 빈공간 있을 때
    temp=0
    far=0
    for j in pli: #j=현재 꽂혀 있는 플러그
        if j not in kli[i:]:
        #3.이후 사용할 플러그 없을 때
            temp=j #현재 플러그로 업데이트
            break
        elif kli[i:].index(j) > far:
        #4. 이후 사용할 플러그 있을 때
        #이후 사용될 플러그 중 가장 마지막에 있는 플러그 뽑아야함
            far=kli[i:].index(j)
            #마지막에 사용될 플러그로 업데이트
            temp=j
    pli[pli.index(temp)] = kli[i]
    #temp 업데이트
    c+=1

print(c)
"""

# 게임을 만든 동준이
"""
n = int(input())
nli=list()
c=0
for i in range(n):
    nli.append(int(input()))

for j in range(n-1,0,-1):
#제일 뒤부터 맨 앞까지 거꾸로, 제일 앞 부터 하는 것보다 효율적
    if nli[j] <= nli[j-1]:
    #제일 뒤 값이 그 앞 값보다 작을 때
        c+=(nli[j-1]-nli[j]+1)
        #그 앞 값에서 뒤 값을 빼면 같아지고, 더 커야 하므로 +1
        nli[j-1]=nli[j]-1
        #제일 뒤 값보다 그 앞 값이 더 작아야 하므로 1만큼 빼주기
print(c)
"""

# 팰린드롬 만들기 : 뒤집어도 똑같은 문자
# Counter 함수 사용
"""
from collections import Counter
name = list(input())
name.sort()
c = Counter(name)
odd = 0
center=''

for i in c: #문자 개수 확인
    if c[i] % 2 !=0: #문자 개수가 홀수이면
        odd+=1 #홀수 +1
        center+=i #홀수인 문자 가운데에
        name.remove(i) #name에서 center에 넣은 문자 remove

if odd>1:
    print("I'm Sorry Hansoo")
else:
    side = ''
    for j in range(0,len(name),2):
        side+=name[j]
    print(side+center+side[::-1])
"""

# 빵집
# 1열~마지막열 까지  파이프라인 최대 개수 출력
# 오른쪽, 오른쪽 위.아래 이동 가능
"""
def go(i,j):
    if j == c-1:
        return True # 마지막열
    for d in dx:
        if 0<=i+d < r and li[i+d][j+1] == '.' and not visit[i+d][j+1]:
        # 시작행+(-1,0,1) < r 이고 [시작행+(-1,0,1)][1,2,3..] =='.' 이고 방문하지 않은 좌표라면
            visit[i+d][j+1] = True #방문
            if go(i+d,j+1):
                return True
    return False

r,c = map(int,input().split())
li = [list(input().rstrip())for _ in range(r)] #입력된 값 리스트
visit = [[False]*c for _ in range(r)] #li * False
dx = [-1,0,1] #방향
ans=0
for i in range(r):
    if li[i][0] == '.':
        if go(i,0):
            ans+=1
print(ans)
"""

# 통나무 건너뛰기
"""
t = int(input())
#제일 큰 숫자를 가운데에 배치하고 그 다음 숫자들을 양쪽에 배치

for _ in range(t):
    n = int(input())
    li=list(map(int,input().split()))
    li.sort() #오름차순 정렬
    c = 0
    for j in range(2,n): #2~n-1
        c=max(c,abs(li[j]-li[j-2])) #abs=절대값
    print(c)
"""

# 크게 만들기
# 문자열을 정수로 변환, k만큼 삭제 후 출력
# stack / 스택 / LIFO
"""
n, k = map(int,input().split())
s=list(input())
stack=[]
K=k
for i in range(n):
    while K>0 and stack: 
        if stack[-1] < s[i]: 
            stack.pop() 
            K-=1 
        else: break
    stack.append(s[i])
print("".join(stack[:n-k])) 

* k와 K 구별
// 여기까지 코드 밑에는 예시

k=2, stack = 1

k=2, stack[-1]=1 < s[1]=9
stack.pop -> stack= 값x
k=1
stack = 9

k=1, i=2, stack[-1] = 9 > s[2]=2

break
stack=9,2

k=2, stack[-1]=2 < s[3]=4
stack.pop -> stack=> 2제거

따라서 stack에 남아있는 94 출력

"""
"""
#컵홀더
#*S*LL*LL*S*S*LL*

n = int(input())
seat = input()
if "L" not in seat:
    c = seat.count('S')
    print(c)
else:
    cs = seat.count('S')
    cl = seat.count('L')
    cll = seat.count("LL")
    if cl == 2:
        print(cs+cl)
    else:
        print(cs+cll+1)

"""

# 거스름돈
# -1 출력할 경우를 앞으로 빼야 시간 단축
"""
n = int(input())
fc=0
ft=0
if n<2 or n==3:
    print(-1)
elif n%5 != 0:
    if (n%5) % 2 != 0:
        fc= n//5 -1
        ft= (n-(5*fc))//2
        print(fc+ft)
    else:
        fc= n//5
        ft= (n%5)//2
        print(fc+ft)
elif n%5 == 0:
    print(n//5)
"""

# 카드 합체 놀이
# 3 2 6 (3+2)
# 5 5 6
# 4 2 3 1 > 1 2 3 4
# 4 3 3 3 > 3 3 3 4
# 4 6 6 3 > 6 6 3 4
"""
import sys
n, m = map(int,sys.stdin.readline().split())
nli = list(map(int,sys.stdin.readline().split()))

for i in range(m):
   nli.sort()  # 오름차순 정렬
   c = nli[0]+nli[1]
   nli[0] = c
   nli[1] = c

print(sum(nli))

# 위 방법보다는 heap으로 구현했을 때 시간복잡도 Good

import sys
import heapq
input = sys.stdin.readline

n,m = map(int, input().split())

card = list(map(int,input().split()))
heapq.heapify(card)

for i in range(m):
    card1 = heapq.heappop(card)
    card2 = heapq.heappop(card)

    heapq.heappush(card, card1+card2)
    heapq.heappush(card, card1 + card2)
print(sum(card))
"""

# 센서
"""
n = int(input())
k = int(input())
nli = list(map(int,input().split()))
nli.sort()
arr=list()
for i in range(n-1):
    arr.append(nli[i+1]-nli[i])
arr.sort()
#print(nli) : 입력받은 배열 정렬
#print(arr) : nli 각 요소의 차이값 정렬
print(sum(arr[:n-k]))
"""

# 폴리오미노
# replace 함수
"""
board = input()
board = board.replace('XXXX','AAAA')
board = board.replace('XX','BB')

if 'X' in board: #치환했음에도 board에 X가 남아있다면
    print(-1)
else:
    print(board)
"""

# A와B
# 작은것에서 큰것으로 갈때는 역순 고려
"""
s = list(map(str,input()))
t = list(map(str,input()))

while len(s) != len(t):
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t=t[::-1]
if s==t:
    print(1)
else:
    print(0)
"""

# UCPC는 무엇의 약자일까?
"""
s = input()
ucpc = ['U','C','P','C']
length=0
for u in ucpc:
    if u in s: #U,C,P,C가 s에 포함된다면
        length+=1
        s=s[s.index(u)+1:] #포함된 인덱스+1부터 마지막인덱스까지로 설정, 다시 반복
    else: #포함 되지 않는다면
        print('I hate UCPC')
        break
if length==4:
    print('I love UCPC')
"""

#주사위
#2 / 1 2 3 4 5 6
#-> 3면*4(24) + 2면*4(12) + 1면*0(0)= 36
#3 / 1 2 3 4 5 6
#-> 3면*4(24) + 2면*12(36) + 1면*9(9) = 69
#4 / 1 2 3 4 5 6
#-> 3면*4(24) + 2면*20(60) + 1면*28(28) = 112

#3면은 24로 고정 , 2면은 24씩 증가
"""
n = int(input())
diceli = list(map(int,input().split()))
if n==1:
    print(sum(diceli) - max(diceli))
else:
    sli=[min(diceli[0],diceli[5]), min(diceli[1],diceli[4]), min(diceli[2],diceli[3])] #인접한 두 면 중 더 작은 값
    sli.sort() #오름차순 정렬
    n1 = (n-2)*(n-2) + 4*(n-1)*(n-2)
    n2 = (n-2)*4 + (n-1)*4
    n3 = 4

    ans = n1*sli[0] + n2*sum(sli[:2]) + n3*sum(sli)
    print(ans)
"""

#배








