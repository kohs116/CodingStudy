# '(' - 쇠막대기 시작점 , ')' - 쇠막대기 끝점 or 레이저 끝점 - 바로 앞에 여는괄호가 오면 레이저, 아니면 쇠막대기 끝점임
# '('는 무조건 stack.append
# ')'는 앞에 어떤 괄호가 오는 지 보고 '('(레이저)가 오면 stack.pop() 하고 카운팅(sum+=len(stack))
# ')'(쇠막대기)가 오면 stack.pop() 하고 카운팅 (sum+=1)

s = input()  # ((())(...
stack = []
cnt = 0  # 쇠막대기
for i in range(len(s)):
    if s[i] == '(':  # 여는괄호는 append
        stack.append(s[i])
    else:  # 닫는 괄호는 레이저 / 쇠막대기
        stack.pop()
        if s[i - 1] == '(':  # 레이저
            cnt += len(stack)
        else:  # 쇠막대기 (막대기의 마지막 조각 +1)
            cnt += 1
print(cnt)
