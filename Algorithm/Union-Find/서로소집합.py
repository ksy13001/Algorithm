# 서로소 집합 -> 서로 공통 요소가 없는 두 집합
# 서로소 집합 연산 -> union, find
# union : 두개의 원소가 포함된 집합 하나로 합침
# find : 특정 원소가 속한 집합 리턴


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
