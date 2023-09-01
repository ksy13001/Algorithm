n = int(input())
k = int(input())
arr = list(map(int, input().split()))
arr.sort()
gap = [arr[i+1]-arr[i] for i in range(n-1)]
gap.sort(reverse=True)
print(sum(gap[k-1:]))
