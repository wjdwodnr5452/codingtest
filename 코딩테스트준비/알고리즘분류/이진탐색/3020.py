import sys

def binary_search

n, h = map(int, sys.stdin.readline().split())

bottom_arr = []
top_arr = []

for i in range(n) :
    if(i % 2 != 0) :
         bottom_arr.append(int(sys.stdin.readline()))
    else :
         top_arr.append(int(sys.stdin.readline()))

bottom_arr.sort()
top_arr.sort()

result_arr = []

for i in range(n) :
     print()
