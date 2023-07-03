# ord('A') = 65
king, pawn, n = map(str, input().split())
king = [ord(king[0])-64, int(king[1])]
pawn = [ord(pawn[0])-64, int(pawn[1])]
c = {'R':(1, 0), 'L':(-1, 0), 'B':(0, -1), 'T':(0, 1), 'RT':(1, 1), 'LT':(-1, 1), 'RB':(1, -1), 'LB':(-1, -1)}
for _ in range(int(n)):
    s = input()
    x, y = c[s][0], c[s][1]
    nx = king[0] + x
    ny = king[1] + y
    if 1 <= nx <= 8 and 1 <= ny<= 8:
        king[0] += x
        king[1] += y
        if king == pawn:
            if 1 <= pawn[0] + x <= 8 and 1 <= pawn[1] + y <= 8:
                pawn[0] += x
                pawn[1] += y
            else:
                king[0] -= x
                king[1] -= y
print((chr(king[0]+64)+str(king[1])))
print((chr(pawn[0]+64)+str(pawn[1])))
