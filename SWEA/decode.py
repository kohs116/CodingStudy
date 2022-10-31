# 문제 요약
# 1. 표1을 보고 입력받은 문자들을 각각 대응하는 숫자로 변경한다.
# 2. 각 숫자들을 6자리 이진수로 표현하고, 이 이진수들을 한 줄로 쭉 이어 붙인다.
# 3. 한 줄로 쭉 이어붙인 이진수들을 8자리씩 끊어서 십진수로 바꾼다.
# 4. 각각의 십진수를 아스키 코드로 변환한다.
# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
# 000000~111111
Decoding = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']
for i in range(1, T + 1):
    t = list(input())
    ans1 = ''
    for j in range(len(t)):
        number = Decoding.index(t[j])  # 입력받은 문자를 숫자로 변환 T->19
        num2 = str(bin(number)[2:])  # 숫자를 2진수로 변환, 값 더하는 것이 아니므로 str변환 19->10011
        while len(num2) < 6:  # 최대가 111111이므로 여섯자리보다 작으면 앞에 0 채워넣기
            num2 = '0' + num2  # 010011_000110
        ans1 += num2  # 2진수 이어붙이기
    r=''
    for k in range(len(t) * 6 // 8):
        e = int(ans1[k * 8:k * 8 + 8], 2)
        r += chr(e)
    print('#{} {}'.format(i, r))










