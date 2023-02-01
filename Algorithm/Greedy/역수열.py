# seq 배열 선언하고 앞에있는 숫자 개수대로 채워넣음
# 만약 이미 들어가 있으면 점점 뒤로 가면서 처리
# n= 8
# a = 5 3 4 0 2 1 1 0
# 4 8 6 2 5 1 3 7

n = int(input())
a = list(map(int, input().split()))
seq = [0] * n
for i in range(n): #정렬된 숫자
    for j in range(n):
        if a[i] == 0 and seq[j] == 0:  # 빈공간 확보 했고 바로 뒷자리에 작은 숫자가 차지
            seq[j] = i + 1  # for문을 0부터 돌렸기 때문에 +1
            break
        elif seq[j] == 0:
            a[i] -= 1
for x in seq:
    print(x, end=' ')
