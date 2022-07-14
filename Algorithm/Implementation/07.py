n = input()
if sum(list(map(int, n[0:(len(n)//2)]))) == sum(list(map(int, n[(len(n)//2):len(n)]))):
    print('LUCKY')
else:
    print("READY")
