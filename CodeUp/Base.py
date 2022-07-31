
# 6007 -> print('\"C:Download\\\'hello\'.py\"') -> \출력 시 \\ 사용!


""" a = input()
    b = input()
    print(b)
    print(a) -> 6013 - 문자열 거꾸로 출력 """

""" a, b = input().split()
    a = int(a)
    b = int(b)
    print(a)
    print(b) -> 6015 - split() 사용 시 공백 기준으로 입력 값 나누어 자름 """

""" a, b = input().split(':')
    print(a, b, sep=':') -> 6018 - split(':') 사용 시 : 기준으로 자름, sep=':' 사용 시 : 사이에 두고 값 출력(sep은 seperator 의미) """

""" a = input()
    b = int(a, 16) - 입력받은 a를 16진수로 변환 
    print('%o' % b) -> 6029 """

"""a = ord(input()) - ord()는 어떤 문자의 순서 위치 값 의미, ord(c)는 문자 c를 10진수로 변환한 값
    print(a) -> 6030 """

""" a = int(input())
    print(chr(a)) - chr()은 정수값을 문자 형태로 바꿔줌 -> 6031 """

""" a = ord(input()) - 입력받은 문자 a를 10진수 형태로 변환
    print(chr(a+1)) - ord 변환 후 그 다음 숫자를 chr 통해 다시 문자로 변환 -> 6033 """

""" a = input()
    a = float(a)
    print(format(a, ".2f")) - format(수, ".2f") 사용 시 원하는 자리까지 반올림 -> 6042 """

""" a, b = input().split()
    a= int(a)
    b= int(b)

    print(a+b)
    print(a-b)
    print(a*b)
    print(a//b)
    print(a%b)
    print(format(a/b, ".2f")) - print(round(a/b,2)) 가 모범답안, -> 6044 """

""" a = int(input())
    print(bool(a)) - bool()을 이용하면 True/False 출력, not a 는 반대로 출력 -> 6052 """

""" a, b = map(int, input().split())
    print(a ^ b) - 비트연산자 xor ^ 은 숫자가 달라야 True -> 6062 """

""" a, b = map(int, input().split())
    c = (a if (a>b) else b) - x if C else y 의 형태로 작성
    print(c) -> 6063 """

""" a, b, c = map(int, input().split())
    n = (a if a<b else b) if ((a if a<b else b)<c) else c - 정수 중 가장 작은 값 출력
    print(n) -> 6064 """

""" a, b, c = map(int, input().split())
    if a%2 == 0 : - if 조건식
        print(a)
    if b%2 == 0 :
        print(b)
    if c%2 == 0 :
        print(c) -> 6065 """

""" a= 1 - 처음 조건 검사 통과하기 위해 임의 값 설정
    while a!=0 :
        a = int(input())
        if a!=0 :
            print(a) -> 6071 """

""" a = int(input())
    start = 0

    while start<=a : - 정수 1개 입력받아 그 수까지 출력하기 EX) 4 입력 시 0~4 출력
        print(start)
        start += 1 -> 6075 """


""" while True: - 원하는 문자 입력 될 때 까지 반복 출력 / 1.제일 먼저 무한 루프 생성 후 
        a = input() - 2. 무한루프 안에서 입력 받고
        print(a) - 3. 입력 받은 값 그대로 출력
        if a=='q': - 4. 만약 입력 받은 값이 q이면
            break - 반복문 종료 -> 6078 """

""" a = int(input())
    s = 0

    for i in range(a+1) :
        s += i
        if s>=a : - 정수의 합 s가 입력값 a 보다 커지면 i 출력 후 break
            print(i)
            break - 입력 한 정수보다 같거나 작을 때 까지만 계속 더하는 프로그램 -> 6079 """

""" a = input()
    a = int(a, 16) # 입력 값 a를 16진수로 변환

    for i in range(1,16) :
        print('%X'%a,'*%X'%i,'=%X'%(a*i), sep='' ) # '%X'%a 는 a에 저장되어 있는 값을 16진수로 출력 한다는 말 
        # 또는 print("%X*%X=%X"%(n,i,n*i)) 로 작성 가능 
        -> 6081 """

""" a = int(input())

    for i in range(1,a+1) :
     if i%10==3 or i%10==6 or i%10==9 : # 3,6,9 들어간 숫자 판별
            print("X", end='') # 3,6,9 들어간 숫자 출력 후 공백으로 끝냄
        else :
            print(i, end='') # 3,6,9 안 들어간 숫자도 출력 후 공백으로 끝냄 -> 6082 """

""" r, b, g = map(int, input().split())
# 빛 섞어 색 만들기 
    for i in range(0, r) :
        for j in range(0, b) :
            for k in range(0, g) :
                print(i,j,k)

    print(r*b*g) # 마지막 개수 출력 
    -> 6083 """

# 1초동안 마이크로 소리 강약 체크하는 횟수 h (<= 48,000)
# 한 번 체크한 값을 저장할 때 사용하는 비트수를 b (<= 32, 단 8의 배수)
# 좌우 등 소리를 저장할 트랙 개수인 채널 개수를 c (<= 5)
# 녹음할 시간(초) s (<= 6,000)
# 필요한 저장용량 계산 프로그램 작성, MB단위로 바꾸어 출력하며 소수점 첫째자리까지 공백 두고 출력

""" h, b, c, s = map(int,input().split())
    mb = (h*b*c*s)/8/1024/1024

    print("%.1f MB" %mb ) -> 6084 """

# 이미지의 가로해상도 w, 세로해상도 h,한 픽셀을 저장하기 위한 비트 b
# 압축하지 않고 저장하기 위해 필요한 저장용량 계산

""" w, h, b = map(int, input().split())
    mb = (w*h*b)/8/1024/1024

    print("%.2f MB" %mb) -> 6085 """

""" n = int(input()) #입력
    sum = 0  #자연수 합계 초기화
    i = 0  #1+2+3+ ... 더할 자연수 0으로 초기화

    while True:
        sum += i
        i += 1
        if (sum>=n) :
            break

    print(sum) -> 6086 """

""" n = int(input()) #정수 입력 , 추후 출력 시 3의 배수는 제외해야 함

    for i in range(1,n+1) :
        if i%3 == 0:
            continue
        else:
            print(i, end=' ') -> 6087 """

""" a, d, n = map(int, input().split()) # 시작값 a, 등차의 값 d, 몇번째 수 인 지 의미하는 정수 n
    # 1 3 5 입력 시 - 1-4-7-10-13 이므로 13 출력
    # 등차수열의 일반항 = a1 + (n-1)d

    print(a+(n-1)*d) -> 6088 """

""" a, r, n = map(int, input().split())
    # 등비수열 일반항 공식 = a1*r^(n-1)

    print(a*r**(n-1)) -> 6089 """

""" a, m, d, n = map(int, input().split())
    # 시작값, 곱할값, 더할값, 몇번째인지 나타내는 정수 입력

    for i in range(1,n):
        a = a*m+d
    print(a) -> 6090 """

""" # 최소공배수 구하기
    # day는 날 수, a/b/c 는 방문 주기
    a, b, c  = map(int, input().split())
    d = 1

    while d%a!=0 or d%b!=0 or d%c!=0:
        d+=1
    print(d) -> 6091 """

""" # 출석번호 n 번 무작위로 불렀을 때 각 번호(1~23)가 불린 횟수 각각 출력
    n = int(input())
    a = map(int, input().split())

    d=[] # 불린 번호 카운트 위해 리스트 변수 생성

    a = list(a) # map 함수로는 []에 접근할 수 없으므로 list 자료형으로 캐스팅

    for i in range (24):
        d.append(0)

    for i in range (n):
        d[a[i]] += 1 # 불린 번호에 대한 카운트 +1

    for i in range (1,24):
        print(d[i], end=' ') # 카운트한 값 공백두고 출력 -> 6092 """

""" # 출석번호 n번 무작위로 불렀을 때 부른 번호 거꾸로 출력, range(시작,끝,증감)
    n = int(input())
    a = map(int, input().split())

    a = list(a)

    for i in range (n-1,-1,-1): # n-2 n-1 ,,,, 2 1 0 까지
        print(a[i], end = ' ') -> 6093 """

""" # 출석번호 n번 무작위로 불렀을 때 가장 먼저 작은 번호 출력
    n = int(input())
    a = map(int, input().split())

    a = list(a)

    print(min(a)) -> 6094 """

""" # 바둑판에 올려놓을 흰 돌의 개수 n 입력
    # 둘째 줄 부터 n+1번째 줄까지 흰 돌을 놓을 좌표(x,y)가 n줄 입력

    d=[] # 마지막 바둑판 상황 출력 위해 리스트 생성

    for i in range(20):
        d.append([]) # 리스트 안에 다른 리스트 추가
        for j in range(20):
            d[i].append(0) # 리스트 안에 들어있는 리스트 안에 0 채워넣기

    n = int(input()) # 바둑판에 올려놓을 흰 돌 개수

    for i in range(n):
        x, y = input().split() # 흰 돌 좌표 입력
        d[int(x)][int(y)] = 1 # 입력된 좌표는 1로 출력

    for i in range(1, 20): # x좌표
        for j in range(1, 20): # y좌표
            print(d[i][j], end = ' ')
        print() -> 6095 """

""" # 바둑판 십자뒤집기 문제 어렵;;
    # 바둑판 깔려있는 상황 19*19 정수값 입력
    # 십자 뒤집기 횟수(n) 입력
    # 십자 뒤집기 좌표 횟수(n)만큼 입력

    d = [] # 입력할 바둑판 리스트, 깔려있는 상황

    for i in range(19):
        d.append([])  # 리스트 안에 다른 리스트 추가
        for j in range(19):
            d[i].append(0)  # 리스트 안에 들어있는 리스트 안에 0 채워넣기

    for i in range(19): # 생성된 리스트 d에 바둑판 현황 입력
        d[i] = list(map(int, input().split()))

    n = int(input()) # 뒤집기 횟수 입력

    for i in range(n):
        x, y = map(int, input().split()) # n번 만큼 x,y 좌표 입력
        for j in range(19): # x,y 한 번 입력 받을 때 마다 좌표값에 따라 조건문 통해 1/0 넣어줌
            if d[j][y-1] == 0 :
                d[j][y-1] = 1
            else :
                d[j][y-1] = 0

            if d[x-1][j] ==0 :
                d[x-1][j] = 1
            else :
                d[x-1][j] = 0

    for i in range(19): # 위 반복문 종료시 리스트에 속한 좌표 출력
        for j in range(19):
            print(d[i][j], end=' ')
        print() # j 반복문 종료되면 줄바꿈 -> 6096 """

""" # 설탕과자 뽑기
    # 격자판 세로 h, 가로 w, 막대의 개수 n, 각 막대의 길이 l, 막대를 놓는 방향 d, 위치 x,y
    # 첫 줄에 격자판 세로,가로 공백 입력 / 둘째 줄 막대 개수 입력 / 셋째 줄 막대 길이,방향,좌표 입력
    # 격자판 채운 막대의 모양 출력 / 막대에 의해 가려지면 1 아닌경우 0

    h, w = map(int, input().split()) # 격자판 세로,가로 입력
    n = int(input()) # 막대 개수 입력

    ans = [[0]*w for _ in range(h)] # list comprension 사용, 조건만족하는 것만 리스트 생성 가능
    # 가로 w X 세로 h 배열 생성

    for i in range(n):
        l, d, x, y = map(int, input().split()) # 막대 길이,방향,좌표(x,y) 입력
        for j in range(l):
            if d == 0: # 방향 d: 가로는 0 세로는 1
                ans[x-1][y-1+j] = 1
            else:
                ans[x-1+j][y-1] = 1 # -1 하는 이유는 입력좌표 x,y가 1,1부터 시작하기 때문임

    for i in range(w):
        for j in range(h):
            print(ans[i][j], end = ' ')
        print() -> 6097 """

# 성실한 개미, 먹이 미로에서 오른쪽, 아래로만 이동 가능
# 미로 상자의 구조 0(갈 수 있는 곳), 1(벽 또는 장애물), 2(먹이)
# 10*10 미로상자의 구조와 먹이 위치 입력
# 개미가 이동한 경로 9로 표시해 출력

array = [] # 2차원 배열
for i in range(10): # 10*10 배열 입력 받음
    array.append(list(map(int, input().split())))

x, y = 1, 1 # 좌표는 1,1부터 시작

while True:
    if array[x][y] == 0 :
        array[x][y] = 9 # 1.현재 칸 0이라면 9로 변환
    elif array[x][y] == 2 :
        array[x][y] = 9 # 2.현재 칸 2라면 반복문 종료
        break

    if array[x][y + 1] == 1 and array[x + 1][y] == 1 : # 3.오른쪽,아래 모두 1(벽)이면 반복문 종료
        break

    if array[x][y+1] != 1 :
        y = y+1
    elif array[x+1][y] != 1 :
        x = x+1
# 4.오른쪽 1 아니면 x 증가, 아래 1 아니면 y 증가

for i in range (10):
    for j in range(10):
        print(array[i][j], end=' ')
    print()





