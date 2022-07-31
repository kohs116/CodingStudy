""" #2480 주사위3개
a, b, c = map(int, input().split())
# 주사위 3개의 눈

if a == b == c:
    print(10000 + (a * 1000))
elif a==b or a==c :
    print(1000 + a * 100)
elif b==c:
    print(1000+ b * 100)
else:
    print(max(a,b,c)*100) """

""" #2525 오븐시계
# 현재 날짜.시간 가져오기 - datetime 모듈 사용

#from datetime import datetime
#now = datetime.now()
#print(now.hour, now.minute)

h, m = map(int,input().split())
t = int(input()) # 요리하는데 걸리는 시간
h += t//60
m += t%60
# // : 나누기 연산 후 소수점 이하의 수를 버리고, 정수 부분의 수만 구함

if m>=60:
    h+=1
    m-=60
if h>=24:
    h-=24

print(h,m) """

""" #2530 인공지능 시계
#알고리즘 순서
#1. 요리하는데 걸린 시간 t를 s에 더함
#2. s를 60으로 나눈 나머지가 다시 s에 저장됨
#3. 2에서 나눈 몫이 m에 저장됨
#4. m을 60으로 나눈 나머지가 m에 저장됨
#5. 4에서 나눈 몫이 h에 저장됨

h, m, s = map(int,input().split()) #시,분,초 공백 입력
t = int(input()) # 요리하는데 필요한 시간(초)

s+=t # 초=초+초
m+=s//60 #분=분+초/60
h+=m//60 #시=시+분/60

print(h%24,m%60,s%60)
# EX) 14 30 0 시작에 200초 입력 - 1. 200초를 0에 더함(s=200) / 2.s를 60으로 나눈 나머지가 다시 s에 저장(s=20)
# 3. 2에서 나눈 몫이 m에 저장(m=30+3=33) / 4,5 3에서 m이 60을 안 넘기므로 생략 - 따라서 14 33 20 출력
# EX2) 17 40 45 시자에 6015초 입력 - 1. s=6015+45=6060 / 2. s=0
# 3. m=101(2에서 나눈 몫)+40=141 / 4. m=141%60=21 / 5.h=17+2(4에서 나눈 몫)=19
# 따라서 19 21 0 출력 """


""" # 2588 곱셈
# 알고리즘
# c=a*b%10 / d=a*(b%100//10) / e=a*(b//100) / ans=c+d+e
a = int(input())
b = int(input())
#곱셈할 두 자연수 입력
print(a*(b%10))
print(a*(b%100//10))
print(a*(b//100))
print(a*b) """

""" #2752 세수정렬
num_list = list(map(int,input().split()))
num_list.sort()
print(num_list[0],num_list[1],num_list[2])
# 숫자 세 개가 주어지므로 0~2 인덱스 출력 """

""" #2753 윤년
#알고리즘 순서
#1. 입력받은 수 a가 4의 배수이면서 100의배수가 아니면 1 출력
#2. a가 4의 배수이면서 400의 배수일 때 1출력
#3. 이외에는 0출력
year = int(input())
if year%4==0 and year%100!=0:
    print(1)
elif year%4==0 and year%400==0:
    print(1)
else: print(0) """

""" #4299 AFC윔블던
#알고리즘 순서
#1. a+b=sum / a-b=sub -> 2a=sum+sub 2b=sum-sub
#2. a=(sum+sub)/2 / b=(sum-sub)/2
#3. 만약 s+m or s-m이 음수이면 -1출력, 합과차 갖는 경기 없어도 -1 출력
#4. 합과차 갖는 경기가 없으려면 a+b+a-b=0 or a+b-a+b=0 이므로 2a=0,2b=0 -> (sum+sub)%2!=0 or (sum-sub)%2!=0

sum, sub = map(int,input().split())
a=int((sum+sub)//2)
b=int((sum-sub)//2)

if sum+sub<0 or sum-sub<0 or (sum+sub)%2!=0:
    print(-1)
else:print(max(a,b),min(a,b)) """

""" #5532 방학숙제
#알고리즘
#1.수학 하루에 최대 D , 국어 하루에 최대 C
#2.k=A/C=국 / m=B/D=수
#3.k랑 m은 반올림해야함 (math.ceil())
#3.k랑 m 비교해서 더 큰 값을 L에서 차감

import math #math.ceil()사용 위해 math모듈 불러옴

L = int(input()) #방학 기간
A = int(input()) #국어 총 페이지
B = int(input()) #수학 총 페이지
C = int(input()) #국어 최대 페이지(하루에)
D = int(input()) #수학 최대 페이지(하루에)

k = math.ceil(A/C)
m = math.ceil(B/D)
print(L-max(k,m)) """

""" #5543 상근날드
#알고리즘
#1.a,b,c 버거 + d,e 콜라와 사이다
#2.a+d or a+e / b+d or b+e / c+d or c+e
#3.2에서 구한 값들 중 가장 작은 값을 출력

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

print(min(a+d, a+e, b+d, b+e, c+d, c+e)-50) """

""" #5575 타임 카드
#알고리즘
#1. 출(시,분,초)=fh,fm,fs / 퇴(시,분,초)=fh,fm,fs
#2. for문으로 3명 반복 계산
#3. 출근시간을 초단위로 계산하여 합하면 first=fs+fm*60+fh*3600 / last=ls+lm*60+ls*3600
#4. t=last-first
#5. h=t//3600 이고 m=(t%3600)//60 이고 s=(t%3600)%60
#6. h,m,s 출력

for i in range(3):
    fh, fm, fs, lh, lm, ls = map(int,input().split())
    first = fs + (fm * 60) + (fh * 3600)
    last = ls + (lm * 60) + (lh * 3600)
    t = last - first
    h = t // 3600 % 24
    m = (t % 3600) // 60
    s = (t % 3600) % 60

    print(h,m,s) """

""" #5596 시험 점수
a, b, c, d = map(int,input().split())
e, f, g, h = map(int,input().split())
mg = int(a+b+c+d)
ms = int(e+f+g+h)

if mg>=ms:
    print(mg)
else:print(ms) """

""" #5893 17배
N = int(input(),2)
ans = N*17
print(format(ans,'b')) """

""" #9498 시험 성적
s = int(input()) #시험 점수 입력
if s>=90 and s<=100:
    print('A')
elif s>=80 and s<=89:
    print('B')
elif s>=70 and s<=79:
    print('C')
elif s>=60 and s<=69:
    print('D')
else: print('F') """

""" #10039 평균 점수
sum=0
for i in range(5):
    s = int(input())
    if s<40:
        sum+=40
    else:
        sum+=s
print(int(sum/5)) """

""" #10101 삼각형 외우기
a = int(input())
b = int(input())
c = int(input())
sum = a+b+c
if a==b==c:
    print("Equilateral")
elif sum==180 and (a==b or a==c or b==c):
    print("Isosceles")
elif sum==180 and (a!=b!=c):
    print("Scalene")
else:print("Error") """

""" #10156 과자
#알고리즘
#1. (k*n)-m
#2. 1번 식이 양수이면 그대로 출력, 음수이면 0 출력
k, n, m = map(int,input().split())
r = (k*n)-m
if r>0:
    print(r)
else:print(0) """

""" #10162 전자레인지
#알고리즘
#1. A:5분=300초 B:1분=60초 C:10초
#2. T%10!=0 이면 -1출력
#3. t//300 t%300//60 t%300%60//10 각각 출력

t = int(input()) #요리시간(초) 입력
if t%10 != 0:
    print(-1)
else:
    A = t //300
    B = (t%300)//60
    C = (t%300)%60 // 10
    print(A,B,C) """

""" #10707 수도요금
#알고리즘
#1. X=P*A Y=B(if P<=C) / Y=B+((P-C)*D)
#2. min(X,Y) 출력

A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())
X = P*A

if P<=C:
    Y=B
else:Y = B+((P-C)*D)

print(min(X,Y)) """

""" #10768 특별한 날
month = int(input())
day = int(input())

if month==2 and day==18:
    print("Special")

if month<2:
    print("Before")

if month>2:
    print("After")

if month==2:
    if day<18:
        print("Before")
    elif day>18:
        print("After") """

""" #10797 10부제
day = int(input())
n = list(map(int,input().split()))
print(n.count(day))
#n에 day가 몇 개나 있는 지 count """

""" #11282 한글
print(chr(44031+int(input())))

#한글 유니코드 십진수로 44032 부터 시작하므로 int형 변환하고 44031 더해줌
#11172=55203-44032+1
#어떤 글자의 코드 a: (a-44032)//(21*28) =초성의 순서(0~18)
#어떤 글자의 코드 a: ((a-44032)%(21*28))//28 =중성의 순서(0~20)
#어떤 글자의 코드 a: ((a-44032)%(21*28))%28 =종성의 순서(0~27)
#종성은 '없음'부터 시작하므로 종성=0='없음' """

""" #11943 파일 옮기기
#알고리즘
#첫번째 바구니 a=a1+b1, 두번째 바구니 b=a2+b2
#min(a1+b2,b1+a2)

a1, b1 = map(int,input().split())
a2, b2 = map(int,input().split())
print(min(a1+b2,b1+a2)) """

""" #11948 과목선택
#알고리즘
#(물+화+생+지)-min(물,화,생,지) + max(역,지)
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

print(((a+b+c+d)-min(a,b,c,d))+max(e,f)) """

""" #13866 팀 나누기
a, b, c, d = map(int,input().split())
print(abs((a+d)-(b+c)))
#a=0 b,c,d=1 인 경우 결과값이 음수이므로 abs사용해야 함 """

""" #14264 정육각형과 삼각형
#알고리즘
#직각삼각형 비율 = 1:루트3:2 = 1a/2:루트3a/2:a
#넓이 = 1a/2 * 루트3a *1/2 = (루트3*a^2)/4
#루트3=3^1/2
l = int(input())
print(((3**0.5)*l**2)/4) """

""" #14470 전자레인지
#알고리즘
#1. if a<0: t=-a*c+d+e*b
#2. if a>0: t=(b-a)*e

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if a<0:
    t = -a * c + d + e * b
else:
    t = (b-a)*e

print(t) """

""" #14623 감정이입
b1 = int(input(),2) #2진수 입력
b2 = int(input(),2)
print(format(b1*b2,'b'))
#oct():10진수를 8진수로
#hex():10진수를 16진수로
#bin():10진수를 2진수로 """

""" #14681 사분면 고르기
x = int(input())
y = int(input())

if x>0 and y>0:
    print(1)
elif x<0 and y>0:
    print(2)
elif x<0 and y<0:
    print(3)
else: print(4) """

""" #14924 폰 노이만과 파리
#알고리즘
#d/(2*s) = h , h*t=answer

s, t, d = map(int,input().split())
h = d//(s*2)
ans = h*t
print(ans) """

""" #14935 FA
x = int(input())
print('FA') """

""" #15700 타일채우기4
n, m = map(int,input().split())
print((n*m)//2) """

""" #15726 이칙연산
#알고리즘
#1. 제일 큰 수 2개 곱하고 남은 수로 나누기
#2. a*b/c or a/b*c
#3. a는 b or c와 곱해지고 남은 수로 나눠짐

a, b, c = map(int,input().split())
print(a*max(b,c)//min(b,c)) """

""" #15921 수찬은 마린보이야!!
N = int(input())
if N>0:
    n = list(map(int,input().split()))
    ans = sum(n)/N / (sum(n)/N)
    print("%.2f" %ans)
else: print("divide by zero") """

""" #15963 CASIO
N, M = map(int,input().split())
if N==M:
    print("1")
else: print("0") """

""" #16199 나이 계산하기
#알고리즘
#만나이 계산할 때 월 기준으로 계산
y, m, d = map(int,input().split())
ty, tm, td = map(int, input().split())

if m < tm:
    a=ty-y
elif m==tm:
    if d <= td:
        a=ty-y
    else: a=ty-y-1
else:a=ty-y-1

if ty==y:
    b=1
elif ty>y: b=ty-y+1
if ty==y:
    c=0
elif ty>y: c=ty-y

print(a)
print(b)
print(c) """

""" #16204 카드 뽑기
#알고리즘
#min(m,k) + n-max(m,k)
n, m, k = map(int,input().split())
print(min(m,k)+n-max(m,k)) """

""" #16428 A/B-3
a, b = map(int,input().split())
c, d = a//b, a%b
if a!=0 and b<0:
    c, d = c+1, d-b
print(c)
print(d) """

""" #16431 베시와 데이지

br, bc = map(int,input().split())
dr, dc = map(int,input().split())
jr, jc = map(int,input().split())

B = max(abs(jr-br), abs(jc-bc))
#베시는 x,y,대각선으로 이동 가능하므로 행과 열의 차이 절대값의 최대를 구해야함
D = abs(jr-dr) + abs(jc-dc)
#데이지는 x or y좌표만 이동 가능
if B == D:
    print("tie")
elif B < D:
    print("bessie")
else:
    print("daisy") """

""" #16486 운동장 한 바퀴
#2*3.141592*d2 + 2*d1
d1 = int(input())
d2 = int(input())
print(2*3.141592*d2 + 2*d1) """

""" #17356 욱 제
a, b = map(int,input().split())
print(1/(1+10**((b-a)/400))) """

""" #17362 수학은 체육과목 입니다 2
#알고리즘
#엄지=1,9,17,25 ...=> n%8==1
#검지=2,8,10,16 ...=> n%8==2 or n%8==0
#중지=3,7,11,15 ...=> n%8==3 or n%8==7
#약지=4,6,12,14 ...=> n%8==4 or n%8==6
#새끼=5,13,21,29 ..=> n%8==5

n = int(input())

if n%8==1:
    print(1)
elif n%8==2 or n%8==0:
    print(2)
elif n%8==3 or n%8==7:
    print(3)
elif n%8==4 or n%8==6:
    print(4)
elif n%8==5:
    print(5) """

""" #17388 와글와글 숭고한
s, k, h = map(int,input().split())
if (s+k+h)>=100 :
    print("OK")
else:
    if min(s,k,h)==s:
        print("Soongsil")
    elif min(s,k,h)==k:
        print("Korea")
    else: print("Hanyang") """

""" #19698 헛간 청약
#입주하는 공간 l*l이 w*h에 수평 혹은 수직이어야 하므로 각각 나눠준 a,b 로 계산
n, w, h, l = map(int,input().split())
a = w//l
b = h//l
if a*b > n:
    print(n)
else: print(a*b) """

""" #19944 뉴비의 기준은 뭘까?
n, m = map(int,input().split())
if m==1 or m==2 : print("NEWBIE!")
elif m<=n and m!=1 and m!=2 : print("OLDBIE!")
else: print("TLE!") """

""" #20499 Darius님 한타 안 함?
k, d, a = map(int,input().split("/"))
if k+a < d or d==0:
    print("hasu")
else: print("gosu") """

""" #23825 SASA 모형을 만들어보자
#sasa=s*2n + a*2m
n, m = map(int,input().split())
print(min(n//2,m//2)) """

""" #24723 녹색거탑
#n=1: c=2 / n=2: c=4 / n=3: c=8 / n=4: c=16 ...
import math
n = int(input()) #높이
print(int(math.pow(2,n)))
# math.pow(2,n) - 2의 n제곱이며 반환형은 float이므로 int형 변환
# 참고: math.sqrt(4) - 4의 제곱근인 2 반환 """

""" #24883 자동완성
a = input()
if a=='N' or a=='n':
    print("Naver D2")
else: print("Naver Whale") """

""" #25191 치킨댄스를 추는 곰곰이를 본 임스
#a//2 + b
n = int(input())
a, b = map(int,input().split())
if (a//2)+b <=n:
    print((a//2)+b)
else:print(n) """

""" #25238 가희와 방어율 무시
#체감 방어율 = a-(a*(b//100))
a, b = map(int,input().split())
c = int(a-(a*(b/100))) #b//100으로 계산 X!!
if c>=100:
    print(0)
else: print(1) """



