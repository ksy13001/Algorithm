for i in range(1, int(input())+1):
    arr = list(map(int, input().split()))
    n, arr = arr[0], arr[1:]
    arr.sort(reverse=True)
    print('Class', i)
    print(f'Max {max(arr)}, Min {min(arr)}, Largest gap {max(list(map(lambda x, y : y-x, arr[1:], arr[:-1])))}')
