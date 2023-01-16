import heapq as hq
a = []
while True:
    n = int(input())
    if n == -1 :
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(hq.heappop(a)) # 루트노드 출력
    else:
        hq.heappush(a,n) #a라는 리스트에 트리형태로 n값을 넣어줌
