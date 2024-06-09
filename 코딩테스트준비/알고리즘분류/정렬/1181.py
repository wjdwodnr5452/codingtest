import sys

num = int(sys.stdin.readline())

arr = []

for i in range(num):
    arr.append(sys.stdin.readline().strip())

arr.sort(key=lambda x: (len(x), x))

result = list(set(arr))

result.sort(key=lambda x : (len(x), x))

for i in result :
    print(i)



