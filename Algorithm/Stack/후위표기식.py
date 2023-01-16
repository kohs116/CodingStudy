#   3+5*2/(7-2) // 앞의 피연산자 2개
# = 352 * 72 -/+
# = 31072 -/+
# = 3105/+ = 32+ = 5

# +나 - 를 만나면 stack에 넣기
# 이후 *나 / 처럼 더 우선순위가 높은 연산자가 들어오게 된다면 stack에 들어가 있는 연산자 처리 하지 않고 stack에 넣기
# stack에 있던 연산자의 우선순위가 더 높거나 같다면 pop(), 새 연산자 stack에 넣기
# 괄호 사이에 있는 연산자는 우선 처리, 괄호는 pop()

a = input()  # 중위식
stack = []
res = ''  # 출력
for x in a:
    if x.isdecimal():  # 숫자이면
        res += x
    else:
        if x == '(':
            stack.append(x)
        elif x == '*' or x == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(x)
        elif x == '+' or x == '-':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop() #여는 괄호 pop
while stack:
    res += stack.pop()
print(res)
