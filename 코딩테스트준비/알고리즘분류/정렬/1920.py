import sys

num = int(sys.stdin.readline())

arr1 = set(map(int, sys.stdin.readline().split()))

num2 = int(sys.stdin.readline())

arr2 = list(map(int, sys.stdin.readline().split()))

for i in arr2:
    if i in arr1:
        print(1)
    else:
        print(0)