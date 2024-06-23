import sys

n, k = map(int, sys.stdin.readline().split())

mv_arr = []

for i in range(n) : 
    mv = list(map(int, sys.stdin.readline().split()))
    mv_arr.append(mv)

mv_arr.sort()

print(mv_arr)

c_arr = []

for j in range(k) :
    c_arr.append(int(sys.stdin.readline()))

c_arr.sort()

print(c_arr)


