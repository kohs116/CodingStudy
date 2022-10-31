# 키패드 누르기
"""
numbers = list(map(int, (input().split())))
hand = str(input())
dic = {1: [0, 0], 2: [0, 1], 3: [0, 2],
       4: [1, 0], 5: [1, 1], 6: [1, 2],
       7: [2, 0], 8: [2, 1], 9: [2, 2],
       '*': [3, 0], 0: [3, 1], '#': [3, 2]}
l_start = dic['*']
r_start = dic['#']
l = [1, 4, 7, '*']
r = [3, 6, 9, '#']
m = [2, 5, 8, 0]
answer = ''

for i in numbers:
    now = dic[i]
    if i in l:
        answer += 'L'
        l_start = now

    elif i in r:
        answer += 'R'
        r_start = now

    else:
        absl = 0
        absr = 0
        for ld, rd, n in zip(l_start, r_start, now):
            absl += abs(ld - n)
            absr += abs(rd - n)

        if absl < absr:
            answer += 'L'
            l_start = now
        elif absl > absr:
            answer += 'R'
            r_start = now
        else:
            if hand == 'left':
                answer += 'L'
                l_start = now
            else:
                answer += 'R'
                r_start = now
print(answer)
"""

# 없는 숫자 더하기
"""
numbers = list(map(int,input().split()))
answer = 0
numbers.sort()
for i in range(10):
    if i not in numbers:
        answer += i
print(answer)
"""

# 음양 더하기
"""
absolutes = list(map(int,input().split()))
signs = list(map(str,input().split()))
answer = 0
for i in range(len(absolutes)):
    if signs[i] == 'true':
        answer += absolutes[i]
    elif signs[i] == 'false':
        answer -= absolutes[i]
print(answer)
"""

# 폰켓몬
"""
nums = list(map(int,input().split()))
cnt = len(nums)//2
rnums = set(nums)
if cnt == rnums:
    print(cnt)
else:
    print(min(cnt,len(rnums)))
"""
stack1 = [2,7]
stack2 = [4,5]
stack3 = [1]
new_stack = stack1 + stack2 + stack3 # 12457
new_stack.sort(reverse=True)
ind = []
for i in range(len(new_stack)):
    if new_stack[i] in stack1:
        ind.append(1)
        continue
    elif new_stack[i] in stack2:
        ind.append(2)
        continue
    else:
        ind.append(3)
        continue
ans = ''.join(str(s) for s in ind)
print(ans)