def sol():
    dic = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6}
    now = input()
    start = now
    visited = []
    for i in range(36):
        if i == 35:
            s = start
        else:
            s = input()
        if s not in visited:
            visited.append(s)
            x, y = dic[now[0]], int(now[1])
            nx, ny = dic[s[0]], int(s[1])
            if {(x-nx), (y-ny)} in [{-1, 2}, {-2, 1}, {-2, -1}, {1, 2}]:
                now = s
                continue
            else:
                print('Invalid')
                return 0
        else:
            print('Invalid')
            return 0
    print('Valid')
    return 0
sol()
