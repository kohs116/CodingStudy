# 정렬된 리스트에서 mid 값 정하고 더 작은 지 , 큰 지 판별 후 lt/rt 범위 변경
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
lt = 0  # 제일 왼쪽 값
rt = n - 1  # 제일 오른쪽 값
while lt <= rt:  # lt가 더 커지면 탐색 마친것
    mid = (lt + rt) // 2  # mid는 0번부터 시작하는 인덱스임
    if a[mid] == m:
        print(mid + 1)
        break
    elif a[mid] > m:
        rt = mid - 1
    else:
        lt = mid + 1
