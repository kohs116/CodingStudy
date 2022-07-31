""" #2440 별 찍기-3
n = int(input())
for i in range(0,n):
    print("*"*(n-i)) """

""" #2441 별 찍기-4
n=int(input())
for i in range(0,n):
    print(" "*i+"*"*(n-i)) """

""" #2442 별 찍기-5
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"*"*((2*i)-1))
#만약 n=5이면 첫줄에 5-1=4 공백에 2*1-1=1 별1개 출력 """

""" #1546 평균
#입력받은 값 / 입력받은 값 중 제일 큰 값 *100
n = int(input()) # 과목의 개수
s = list(map(int,input().split())) #현재 점수
ms= max(s) #입력받은 값 중 제일 큰 값 ms
sum=0
for i in range(n):
    avg = ((s[i]/ms)*100)/n
    sum+=avg #각 값에대해 구한 avg 더하기
print(sum) """

""" #3460 이진수
n = int(input()) #테스트케이스 입력
for i in range(n):
    a = bin(int(input()))[2:] #입력받은 a를 2진수로 변환, 앞의 두자리 제외
    for i in range(len(a)):
        if a[-i-1] == '1': #-i는 제일 뒤애있는 값 부터 출력, -1은 역"순" 출력
            print(i, end=' ') """





