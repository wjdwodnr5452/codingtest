import sys

n, h = map(int, sys.stdin.readline().split())

arr = []

for i in range(n) :
    arr.append(int(sys.stdin.readline()))

arr.sort()

print(arr)

