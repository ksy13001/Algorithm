import sys
input = sys.stdin.readline
INF = int(1e9)


def build_max_tree(idx, left, right):
    if left == right:
        segment_tree[idx][1] = arr[left]
        return segment_tree[idx][1]
    mid = (left + right)//2
    segment_tree[idx][1] = max(build_max_tree(idx*2, left, mid),  build_max_tree(idx*2+1, mid+1, right))
    return segment_tree[idx][1]


def build_min_tree(idx, left, right):
    if left == right:
        segment_tree[idx][0] = arr[left]
        return segment_tree[idx][0]
    mid = (left + right)//2
    segment_tree[idx][0] = min(build_min_tree(idx*2, left, mid),  build_min_tree(idx*2+1, mid+1, right))
    return segment_tree[idx][0]


def query_max(idx, left, right, start, end):
    if start > right or left > end:
        return 0
    elif start <= left and right <= end:
        return segment_tree[idx][1]
    mid = (left + right)//2
    return max(query_max(idx*2, left, mid, start, end), query_max(idx*2+1, mid+1, right, start, end))


def query_min(idx, left, right, start, end):
    if start > right or left > end:
        return INF
    elif start <= left and right <= end:
        return segment_tree[idx][0]
    mid = (left + right)//2
    return min(query_min(idx*2, left, mid, start, end), query_min(idx*2+1, mid+1, right, start, end))


n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
segment_tree = [[INF, 0] for _ in range(4*n)]
build_max_tree(1, 0, n-1)
build_min_tree(1, 0, n-1)

for _ in range(m):
    a, b = map(int, input().split())
    print(query_min(1, 0, n-1, a-1, b-1), query_max(1, 0, n-1, a-1, b-1))
