# 숫자를 만나면 stack.append
# 연산자를 만나면 stack의 상단부터 두개 빼기 (먼저나온게 뒤로) - 그 결과를 다시 stack.append

a = input()
stack = []
for x in a:
    if x.isdecimal():
        stack.append(int(x))
    else:
        if x == '+':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 + n1)
        elif x == '-':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 - n1)
        elif x == '*':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 * n1)
        else:
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 / n1)
print(stack[0]) #어차피 값 한개만 남아있음
