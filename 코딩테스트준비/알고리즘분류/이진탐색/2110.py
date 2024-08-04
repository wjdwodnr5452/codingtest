import sys

def binary_search(data_list) :
    start = 0

    



n, c = map(int, sys.stdin.readline().split())

arr = []

for i in range(n) :
    arr.append(int(sys.stdin.readline()))

arr.sort()

result = binary_search(arr)


