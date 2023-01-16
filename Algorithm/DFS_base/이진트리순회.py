def DFS(v):
    if v > 7:
        return
    else:
        #print(v, end=' ')  # 전위순회 (본인 처리 하고 넘어감)
        DFS(v * 2)  # 왼쪽 노드
        #print(v, end=' ') # 중위순회 (왼쪽 먼저 처리하고 본인)
        DFS(v * 2 + 1)  # 오른쪽 노드
        print(v, end=' ') # 후위순회 (왼쪽 하고 오른쪽 하고 되돌아와서 본인)
        #후위순회를 쓰는 대표적인 경우는 병합정렬
        #대부분은 전위순회 사용

if __name__ == "__main__":
    DFS(1)  # v=1
