T = int(input())
for tc in range(1, T + 1):
    n = int(input())  # 2
    li = [0] * 10  # 0 0 0 0 0 0 0 0 0 0
    i = 0
    while (True):
        if 0 not in li:
            break
        else:  # 0 in li
            i += 1  # i=1
            num = str(n * i)  # 2
            for j in range(len(num)):  # 0
                li[int(num[j])] = 1  # 해당 인덱스에 1넣기
    print("#{} {}".format(tc, num))
