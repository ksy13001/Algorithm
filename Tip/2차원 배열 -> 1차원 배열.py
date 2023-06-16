import itertools
# sum(iterable, start)
# iterable -> 반복 가능한 객체, list, dict, set, str, bytes, tuple, range
arr = [[1, 3], [2, 4], [3, 5]]
arr1 = sum(arr, [])
print(arr1)
arr2 = list(itertools.chain(*arr))    # *붙여 줘야함
print(arr2)
