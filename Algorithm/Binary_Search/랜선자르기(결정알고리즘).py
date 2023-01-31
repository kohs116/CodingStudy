# 제일 긴 값을 정한 뒤 이분검색
def Count(len):
    cnt = 0
    for x in Line:
        cnt += (x // len)  # 몫 구하기
    return cnt


k, n = map(int, input().split())
Line = []
res = 0
largest = 0
for i in range(k):
    tmp = int(input())
    Line.append(tmp)
    largest = max(largest, tmp)  # 제일 긴 값
lt = 1
rt = largest
while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= n: #나눈 몫이 n개보다 많으면 줄여야함
        res = mid
        lt = mid + 1 #줄이기 위해 lt 조정
    else:
        rt = mid - 1
print(res)
