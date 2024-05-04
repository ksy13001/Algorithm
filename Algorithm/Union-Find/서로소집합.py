
def find(parents, x): # x의 부모 찾기
    if parents[x] != x:
        return find(parents, parents[x]) # x
    else:
        return x


def union(parents, a, b):   # a, b 합치기
    a = find(parents, a)
    b = find(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b
