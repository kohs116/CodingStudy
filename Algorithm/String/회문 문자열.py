# 문자를 앞으로 읽어도 뒤로 읽어도 똑같으면 YES , 다르면 NO 출력
# 대소문자 구분 X
"""
n = int(input())

for i in range(n):
    s = input()
    s = s.upper()  # 문자열 대문자화, lower()해도 됨
    size = len(s)
    for j in range(size // 2):  # 길이가 홀수면 가운데 문자는 비교할 필요 없음, ex) len=5 이면 0,4 2,3 각각 비쇼
        if s[j] != s[-1 - j]: # 인덱스 -1,-2,, 접근
            print("#%d NO" % (i + 1))
            break
    else:
        print("%d YES" % (i + 1))

"""
n = int(input())

for i in range(n):
    s = input()
    s = s.upper()  # 문자열 대문자화, lower()해도 됨
    if s == s[::-1]:
        print("%d YES" % (i + 1))
    else:
        print("%d NO" % (i + 1))
