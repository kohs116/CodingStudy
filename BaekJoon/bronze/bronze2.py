""" #5598 카이사르 암호
#알고리즘
#입력받은 문자 s를 ord함수를 사용하여 숫자로 변환
#변환된 숫자-3 하고 chr함수 사용해서 문자 출력
s = list(input())
for i in range(len(s)):
    rs = ord(s[i])-3 #문자열의 각 문자를 숫자로 변환
    if rs < ord('A'): #만약 A,B,C 입력 받을 시
        rs+=26 #26 더해줌
    s[i]=chr(rs) #다시 문자로 변환
print("".join(s)) #리스트를 문자열로 출력 시 join """

""" #2562 최댓값
n=[] #입력받을 숫자를 리스트로
for i in range(9): #9개 자연수 입력받기
    n.append(int(input())) #여러개의 입력값 줄바꿈하여 리스트로 받기
print(max(n))
print(n.index(max(n))+1) #0~8 인덱스 중 최댓값의 인덱스 출력 """

""" #10809 알파벳 찾기
s = input()
a = 'abcdefghijklmnopqrstuvwxyz'
# a = list(range(97,123)) : 영어 소문자 아스키코드 97~122
for i in a: #a~z 검사
    if i in s: #s에 a 존재하면 index 출력
        print(s.index(i), end=' ')
    else: print(-1, end=' ') """



