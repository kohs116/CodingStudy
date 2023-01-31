# 격자판에서 본인의 상하좌우 숫자보다 큰 숫자는 봉우리 지역, 지역이 몇개인 지 출력
dx = [-1, 0, 1, 0]  # i=-1,0,1,0 - 상 우 하 좌
dy = [0, 1, 0, -1]  # j=0,1,0,-1
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.insert(0, [0] * n)  # 0번 행에 [0] 채워넣기
a.append([0] * n)  # 제일 뒤 행에 [0] 채워넣기
for x in a:  # 가장자리
    x.insert(0, 0)
    x.append(0)
cnt = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if all(a[i][j] > a[i + dx[k]][j + dy[k]] for k in range(4)):
            cnt += 1
print(cnt)