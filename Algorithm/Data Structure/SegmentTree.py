# 세그먼트 트리 생성 (Top-down : 재귀)
# 좌측 인덱스 -> idx*2, 우측 인덱스 -> idx*2 + 1
def build_tree(idx, left, right):
    # 왼쪽, 오른쪽 구간 같을때
    if left == right:
        segment_tree[idx] = arr[left]
        return segment_tree[idx]
    mid = (left + right)//2
    segment_tree[idx] = build_tree(idx*2, left, mid) + build_tree(idx*2+1, mid+1, right)
    return segment_tree[idx]


# 세그먼트 트리 업데이트(node -> 업데이트 위치, value -> 업데이트 값)
def update_tree(idx, left, right, node, value):
    # 목표 위치에 도달 하면 값 갱신
    if left == right == node:
        arr[node] = value
        segment_tree[idx] = value
    # 업데이트 인덱스가 구간 안에 있을 경우 재귀적으로 탐색 하기
    elif left <= node <= right:
        mid = (left + right)//2
        update_tree(idx * 2, left, mid, node, value)
        update_tree(idx * 2 + 1, mid + 1, right, node, value)
        segment_tree[idx] =  segment_tree[idx*2] + segment_tree[idx*2+1]


# 세그먼트 트리 쿼리 처리(start, end -> 목표 구간)
def query_tree(idx, left, right, start, end):
    # left = 0, right = 4 / start = 1, end = 4
    if start > right or left > end:
        return 0
    elif start <= left and right <= end:
        return segment_tree[idx]
    mid = (left + right)//2
    return query_tree(idx*2, left, mid, start, end) + query_tree(idx*2+1, mid+1, right, start, end)


arr = [1, 2, 3, 4, 5]
segment_tree = [0] * (4*(len(arr)))

build_tree(1, 0, len(arr)-1)
print('segment tree:',segment_tree)
update_tree(1, 0, len(arr), 2, 10)
print('updated arr:', arr)
print('updated segment tree:',segment_tree)
print('인덱스 1~4 까지의 구간합:',query_tree(1, 0, len(arr)-1, 1, 4))   # 21
