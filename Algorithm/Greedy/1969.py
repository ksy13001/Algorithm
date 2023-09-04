import sys
INF = sys.maxsize
input = sys.stdin.readline
# A : 65 Z : 90


def sol():
    n, m = map(int, input().split())
    word = []
    ans = 0
    ans_word = ''
    for _ in range(n):
        word.append(list(input().rstrip()))
    for j in range(m):
        arr = [0] * 26
        for i in range(n):
            arr[ord(word[i][j])-65] += 1
        max_num = max(arr)
        ans += n-max_num
        ans_word += chr(arr.index(max_num) + 65)
    print(ans_word)
    print(ans)


sol()
