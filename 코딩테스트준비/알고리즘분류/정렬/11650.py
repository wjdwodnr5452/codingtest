import sys

num = int(sys.stdin.readline())

# 1차원
arr1 = []

# 2차원
arr2 = []

for i in range(num):
    m, n = map(int, sys.stdin.readline().split())
    arr2.append(m)
    arr2.append(n)
    arr1.append(arr2)
    arr2 = []

arr1.sort()

for i in arr1:
    print(*i)





