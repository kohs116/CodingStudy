# 오름차순 정렬 된 두 리스트를 오름차순으로 합쳐서 출력
# sort() 호출하면 시간복잡도 nlogn
# 이미 정렬되어 있다는 사실을 이용하면 n번만에 끝낼 수 있음

# a[p1]과 b[p2] 크기 비교해서 작은 값을 리스트에 append
# append 후 p1+1 (인덱스)
# 만약 값이 같으면 아무거나 append

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

p1 = p2 = 0  # 포인터 변수
c = []
while p1 < n and p2 < m:  # 둘 중 하나라도 n까지 도달하면 끝
    if a[p1] < b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1
if p1 < n:  # a 리스트에 아직 값이 남았다면
    c = c + a[p1:]
if p2 < n:
    c = c + b[p2:]

for x in c:
    print(x, end=' ')
