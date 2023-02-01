# 5 2 7 6 8 2 3
# 순서대로 stack에 넣고, 현재 넣는 값이 이미 stack에 있는 값보다 크면 stack.pop()
# pop()한 횟수가 주어진 숫자와 같아지면 break

num, m = map(int, input().split())
num = list(map(int, str(num)))  # string 변환해서 값 하나하나를 숫자화
stack = []
for x in num:
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1
    stack.append(x)
if m != 0:
    stack = stack[:-m]
res = ''.join(map(str, stack))  # string join
print(res)
