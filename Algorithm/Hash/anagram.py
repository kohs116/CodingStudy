# 두 단어의 문자 나열 순서는 다르지만 구성이 일치하면 아나그램 YES
# key-value 알파벳-카운팅
# str1.get('A',0) -> A라는 key값이 없으면 0리턴, 있으면 value 리턴
"""
a = input()
b = input()
str1 = dict()
str2 = dict()
for x in a:
    str1[x] = str1.get(x, 0) + 1
for x in b:
    str2[x] = str2.get(x, 0) + 1
for i in str1.keys(): # str1의 key 값
    if i in str2.keys():
        if str1[i] != str2[i]: # 카운팅 수가 다르면
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")
"""
"""
a = input()
b = input()
sH = dict()
for x in a:
    sH[x] = sH.get(x, 0) + 1
for x in b:
    sH[x] = sH.get(x, 0) - 1  # value 값 0 만들기
for x in a:
    if sH.get(x) > 0:
        print("NO")
        break
else:
    print("YES")
"""
# 여기까지는 Dictionary Hash

a = input()
b = input()
str1 = [0] * 52
str2 = [0] * 52  # 총 알파벳 수 52
for x in a:
    if x.isupper():
        str1[ord(x) - 65] += 1  # 65(A)~90(Z) 97(a)~122(z)
    else:
        str1[ord(x) - 71] += 1
        # 0(A)~25(Z) 26(a)~51(z) 소문자는 71(97-26)을 빼줘야 26 인덱스부터 시작 가능
for x in b:
    if x.isupper():
        str2[ord(x) - 65] += 1
    else:
        str2[ord(x) - 71] += 1
for i in range(52):
    if str1[i] != str2[i]:
        print("NO")
        break
else:
    print("YES")
