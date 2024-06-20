import sys

n, m = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

num = arr[0] + m
count = 1

for i in arr[1:]:
    if(num <= i):
        count += 1
        num = i+m

print(count)



