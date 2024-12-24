n = int(input('Enter the no. of elements in array : '))
arr = set((map(int, input().split())))
a = sorted(arr)
print(f'The runner up is : {a[-2]}')