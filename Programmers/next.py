n = int(input())
answer = 0
n_to_bin = bin(n)
bin_count = n_to_bin.count('1')

for i in range(1, n):
    new_n = n
    new_n += i
    new_bin = bin(new_n)
    new_count = new_bin.count('1')
    if bin_count == new_count:
        print(new_n)
        break
    else:
        continue