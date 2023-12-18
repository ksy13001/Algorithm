import sys
input = sys.stdin.readline


def update_tree(idx, left, right, node, value):
    if left == right == node:
        arr[node] = value
        segment_tree[idx] = value
    elif left <= node <= right:
        mid = (left + right)//2
        update_tree(idx * 2, left, mid, node, value)
        update_tree(idx * 2 + 1, mid + 1, right, node, value)
        segment_tree[idx] =  segment_tree[idx*2] + segment_tree[idx*2+1]


def query_tree(idx, left, right, start, end):
    if start > right or left > end:
        return 0
    elif start <= left and right <= end:
        return segment_tree[idx]
    mid = (left + right)//2
    return query_tree(idx*2, left, mid, start, end) + query_tree(idx*2+1, mid+1, right, start, end)


n, m = map(int, input().split())
arr = [0] * n
segment_tree = [0] * (4*n)
for _ in range(m):
    mode, a, b = map(int, input().split())
    # Sum
    if mode == 0:
        if a > b:
            a, b = b, a
        print(query_tree(1, 0, len(arr)-1, a-1, b-1))
    # Modify
    else:
        update_tree(1, 0, len(arr)-1, a-1, b)
