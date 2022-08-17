from bisect import bisect_left, bisect_right

num = [1, 2, 3, 3, 4, 5]
k = 3
l = bisect_left(num, k)   #k 값 왼쪽  인덱스 반환
r = bisect_right(num, k)  #k 값 오르쪽 인덱스 반환

print(l) #2
print(r) #4
