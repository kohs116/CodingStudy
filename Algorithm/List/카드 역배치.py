# 1~20 까지 적힌 카드가 순서대로 놓여있다. 주어진 구간 a,b 사이의 카드를 역순으로 놓는다.
# 최종 카드 순서 출력

card = list(range(21))
for _ in range(10):  # 20장이기 때문에 최대 10
    s, e = map(int, input().split())
    for i in range((e - s + 1) // 2):
        card[s + i], card[e - i] = card[e - i], card[s + i]

card.pop(0)  # 맨 앞 인덱스 값인 '0' pop()

for x in card:
    print(x, end=' ')
   