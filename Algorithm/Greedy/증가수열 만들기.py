# 2 4 5 1 3 주어지면 왼쪽 끝(lt)에서 2, 오른쪽 끝(rt)에서 3, lt에서 4,5 가져오면
# 2 3 4 5 의 길이 4인 증가수열 만들기 가능
# 만들고 있는 증가수열 last 값 갱신 하며 lt,rt 조정

n = int(input())
a = list(map(int, input().split()))
lt = 0
rt = n - 1
last = 0
res = ""  # 문자열 출력
tmp = []  # 정렬할 리스트
while lt <= rt:
    if a[lt] > last:
        tmp.append((a[lt], 'L'))  # 튜플값 append
    if a[rt] > last:
        tmp.append((a[rt], 'R'))
    tmp.sort()
    if len(tmp) == 0:
        break  # 수열의 마지막 항보다 양 왼,오른쪽 끝 자료가 더 작음
    else:
        res = res + tmp[0][1]  # 문자열 더하기
        last = tmp[0][0]
        if tmp[0][1] == 'L':
            lt += 1
        else:
            rt -= 1
    tmp.clear()
print(len(res))
print(res)
