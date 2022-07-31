""" #10828 스택
import sys
n = int(sys.stdin.readline())
stack = []
for i in range(n):
    s = sys.stdin.readline().split()
    if s[0]=='push':
        stack.append(s[1])
    elif s[0]=='pop':
        if len(stack)==0:
            print(-1)
        else: print(stack.pop())
    elif s[0]=='size':
        print(len(stack))
    elif s[0]=='empty':
        if len(stack)==0:
            print(1)
        else: print(0)
    elif s[0]=='top':
        if len(stack)==0:
            print(-1)
        else: print(stack[-1]) """

""" #10845 큐
import sys
n = int(sys.stdin.readline())
queue = []
for i in range(n):
    s = sys.stdin.readline().split()
    if s[0]=='push':
        queue.insert(0,s[1]) #s[1]을 맨 앞에 추가
        #print(queue)
    elif s[0]=='pop':
        if len(queue)==0:
            print(-1)
        else: print(queue.pop())
    elif s[0]=='size':
        print(len(queue))
    elif s[0]=='empty':
        if len(queue)!=0:
            print(0)
        else: print(1)
    elif s[0]=='front':
        if len(queue)==0:
            print(-1)
        else: print(queue[len(queue)-1])
    elif s[0]=='back':
        if len(queue)==0:
            print(-1)
        else: print(queue[0]) """

#10866 덱: 큐의 앞과 뒤 모두에서 삽입 및 삭제가 가능한 큐
from collections import deque
import sys
n = int(sys.stdin.readline())
d=deque()
for i in range(n):
    s = sys.stdin.readline().split()
    if s[0]=='push_front':
        d.appendleft(s[1])
    elif s[0]=='push_back':
        d.append(s[1])
    elif s[0]=='pop_front':
        if len(d)==0:
            print(-1)
        else: print(d.popleft())
    elif s[0]=='pop_back':
        if len(d)==0:
            print(-1)
        else: print(d.pop())
    elif s[0]=='size':
        print(len(d))
    elif s[0]=='empty':
        if len(d)==0:
            print(1)
        else: print(0)
    elif s[0]=='front':
        if len(d)==0:
            print(-1)
        else: print(d[0])
    elif s[0]=='back':
        if len(d)==0:
            print(-1)
        else: print(d[-1])




