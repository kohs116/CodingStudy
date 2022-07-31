"""
def solution(participant, completion):
    participant.sort()
    completion.sort() #참가자, 완주자 모두 정렬
    for p,c in zip(participant, completion): #zip함수 이용하여 인덱스별로 비교
        if p != c:
            return p
    return participant[-1] # 마지막 사람 출력
"""


""" # 만약 겹치는 문자열 있으면 false, 그렇지 않다면 true 반환

def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True """

