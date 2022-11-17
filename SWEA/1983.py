
#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for tc in range(1, T + 1):
    n,k = map(int,input().split()) #학생수 n, 학생번호 k
    score_sum = [] #각 학생의 총점을 저장할 리스트

    for i in range(n):
        m, f, r = list(map(int, input().split()))  # 중간, 기말, 과제 점수 입력받기
        score = m*0.35 + f*0.45 + r*0.20 #총점
        score_sum.append(score)
    k_score = score_sum[k-1] #k번째 학생의 총점
    score_sum.sort(reverse=True) #총점 내림차순 정렬
    d = n//10 #grades 구분
    answer = score_sum.index(k_score) // d
    print('#{} {}'.format(tc,grades[answer]))


