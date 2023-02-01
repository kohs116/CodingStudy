# DVD에 총 N개의 곡이 들어가고 , M개의 DVD에 모든 동영상 녹화
# 최대 용량을 판별하여 출력
# lt=1, rt=총 용량
# 답이 여러 개일 수 있으므로 갱신 해 주어야 함
def Count(capacity):
    cnt = 1
    sum = 0  # 곡 들의 누적 시간
    for x in Music:
        if sum + x > capacity: #누적 시간 합이 설정값 mid보다 크면
            cnt += 1
            sum = x #초기화
        else:
            sum += x
    return cnt


n, m = map(int, input().split())
Music = list(map(int, input().split()))
maxx=max(Music)
lt = 1
rt = sum(Music)
res = 0
while lt <= rt:
    mid = (lt + rt) // 2
    if mid>=maxx and Count(mid) <= m: #최소한 가장 큰 용량을 가지는 dvd 보다는 커야함
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1
print(res)
