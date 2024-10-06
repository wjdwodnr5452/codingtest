import sys

n = int(sys.stdin.readline())

arr = []

for i in range(n) :
    arr.append(int(sys.stdin.readline()))

arr.sort()

result = 0

for i in range(1, n+1) : 
    result += abs(i-arr[i-1])

print(result)
