# (문자+숫자) 문자열에서 숫자만 추출하여 그 순서대로 자연수 만들기
# 만들어진 자연수와 그 자연수의 약수 개수 출력

s = input()
res = 0
for i in s:
    if i.isdecimal():  # isdecimal은 숫자 0~9, isdigit은 숫자형태면 모두 인식
        res = res * 10 + int(i)  # 숫자화
print(res)
cnt = 0
for j in range(1, res + 1):  # 약수 구하기
    if res % j == 0:
        cnt += 1
print(cnt)
