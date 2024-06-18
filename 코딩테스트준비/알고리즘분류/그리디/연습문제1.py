import sys

arr = [500, 100, 50, 10]
n = int(sys.stdin.readline())
count = 0

for i in arr:
    count += n // i
    n %= i

print(count)