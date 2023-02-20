def DFS(len):
    if dy[len] > 0:
        return dy[len]  # 메모이제이션

    if len == 1 or len == 2:  # 1m 자르는 방법 1, 2m 자르는 방법 2
        return len
    else:
        dy[len] = DFS(len - 1) + DFS(len - 2)
        # dy[7] = D(6) + D(5)
        return dy[len]


if __name__ == "__main__":
    n = int(input())
    dy = [0] * (n + 1)
    print(DFS(n))
