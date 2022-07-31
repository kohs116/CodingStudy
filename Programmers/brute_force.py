""" 모의고사
def solution(answers):
    answer = []  # 가장 많이 맞힌 사람(출력)
    a = [1, 2, 3, 4, 5]  # 1번 수포자가 찍는 방식
    b = [2, 1, 2, 3, 2, 4, 2, 5]  # 2번
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 3번

    s = [0, 0, 0]  # a,b,c가 각각 문제 맞은 개수

    for i in range(len(answers)):
        if answers[i] == a[i % 5]:  # T=5 / 정답이 들어있는 배열과 a가 찍는 방식 같은 지 확인
            s[0] += 1  # 같으면 문제맞은 개수 배열에 +1
        if answers[i] == b[i % 8]:  # T=8
            s[1] += 1
        if answers[i] == c[i % 10]:  # T=10
            s[2] += 1

    s_max = max(s)  # a,b,c가 문제 맞은 개수 배열에서 가장 많이 맞힌 개수

    for i in range(3):
        if s_max == s[i]:  # a,b,c중 가장 많이 맞힌 개수가 누구인 지 확인
            answer.append(i + 1)  # 확인 되면 맞힌 사람 출력하는 배열 answer에 i+1(+1은 1~3출력을 위함)
    return answer
"""

""" from itertools import permutations #소수 판별 함수
def is_prime_number(x):
    if x<2:
        return False
    for i in range(2,x):
        if x%i ==0 :
            return False
    return True

def solution(numbers):
    answer = 0 #조합해서 소수가 몇 개 나오는 지
    n = [] #numbers 자름
    for i in range(1,len(numbers)+1): #순열 조합
        n.append(list(set(map(''.join,permutations(numbers,i)))))
        #numbers를 자른 배열 n에 순열조합한 결과를 넣음
        #조합한 결과를 '1' '2' 와 같이 작은따옴표로 묶음
    p = list(set(map(int,set(sum(n,[])))))
    #sum(n,[])하면 '1' '2' 를 [1,2] 로 묶어줌
    #중복제거 위해 set함수 사용
    #p를 n에 넣기위해 list로 변환
    for i in p:
        if is_prime_number(i)==True:
            answer+=1
    return answer """


""" 카펫
def solution(brown, yellow):
    answer = []
    s = brown + yellow
    for y in range(1, s + 1):
        if (s % y) == 0:  # s%y==0: s/y=12,6,4,3,2,1=x
            x = s / y
            if x >= y:
                if 2 * x + 2 * y == brown + 4:
                    # (x-2)*(y-2) = brown+4 = 2*x+2*y
                    return [x, y]
    return answer """
