def solution(citations):
    citations.sort(reverse=True)
    for idx , citation in enumerate(citations):
        #idx = 0,1,2 .. citation = citations배열
        if idx >= citation:
            return idx
    return len(citations)