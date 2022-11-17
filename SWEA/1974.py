T = int(input())
stack = []
for tc in range(1, T + 1):
    arr = [list(map(int,input().split())) for i in range(9)]
    for col in range(9):
        for c in arr[col]:
            if c in stack:
                print(0)
                break
            else:
                stack.append(c)


