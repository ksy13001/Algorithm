 
def sol():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    visited = [0] * k
    cnt = 0
    # MEX -> 현재 배열의 요소들을 제외하고 최소값
    # MEX(arr) = k -> arr의 현재 요소들을 제외하고 최소값이 k
    # 1. arr 에서 k 없어야함 -> k-1로 바꾼다고 생각
    # 2. arr 에서 한번도 나오지 않고 k - 1 보다 작은값 있으면 안됨
 
    for i in arr:
        if i < k:
            visited[i] += 1
        if i == k:
            cnt += 1
 
    print(cnt + max(0, visited.count(0)-cnt))
 
 
t = int(input())
for i in range(t):
    sol()
