def solution():
    s = input()
    a = 0
    b = 0
    ans = 0
    for st in s:
        if st == "A":
            a += 1
        elif st == "B":
            if a > 0:
                a -= 1
                b += 1
        elif st == "C":
            if b > 0:
                b -= 1
                ans += 1
    print(ans)

solution()
