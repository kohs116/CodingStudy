"""
from heapq import heappop, heappush

def solution(book_time):
    answer = 1
    book_time_res = [(int(s[:2]) * 60 + int(s[3:4]), int(e[:2]) * 60 + int(e[3:4])) for s, e in book_time]
    book_time_res.sort()

    heap = []
    for s, e in book_time_res:
        if not heap:
            heappush(heap, e)
            continue
        if heap[0] <= s:
            heappop(heap)
        else:
            answer += 1
        heappush(heap, e + 10)

    return answer
"""

def timeToval(time):
    return int(time[:2])*60 + int(time[3:5])
    # 분 단위 변환

def solution(book_time):
    dic = {}
    for i in book_time:
        start = timeToval(i[0])
        end = timeToval(i[1])
        for j in range(start,end+10):
            if dic.get(j) == None:
                dic[j] = 1
            else:
                dic[j] += 1
    return max(dic.values())
