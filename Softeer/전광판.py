import sys

T = int(input())

nums = {'0': '1110111',
        '1': '0010010',
        '2': '1011101',
        '3': '1011011',
        '4': '0111010',
        '5': '1101011',
        '6': '1101111',
        '7': '1110010',
        '8': '1111111',
        '9': '1111011',
        ' ': '0000000'}

for k in range(T):
    a, b = sys.stdin.readline().split()
    a = (5 - len(a)) * ' ' + a
    b = (5 - len(b)) * ' ' + b

    total = 0
    for i in range(5):
        for j in range(7):
            if nums[a[i]][j] != nums[b[i]][j]:
                total += 1
    print(total)
