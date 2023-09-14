import sys, heapq
#input = sys.stdin.readline


def sol():
    num = 1
    while True:
        st = input()
        if '-' in st:
            return
        q = []
        cnt = 0
        for i in st:
            if not q:
                if i == '}':
                    cnt += 1
                q.append('{')
            else:
                if q[-1] == '{':
                    if i == '}':
                        q.pop()
                    else:
                        q.append(i)
                else:   # '}'
                    if i == '}':
                        cnt += 1
                    else:
                        cnt += 2
                    q.pop()
        print(f'{num}. {cnt + len(q)//2}')
        num += 1


sol()
