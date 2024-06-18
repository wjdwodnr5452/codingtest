import sys

N, K = map(int, sys.stdin.readline().split())

count = 0

while True :
    target = (N // K) * K       # 25  5 0 
    print("target : ",  target)
    count += (N - target)    # 1 2 4
    print("count : ",  count)
    N = target  # 25   5 0

    if N < K :
        break

    count += 1 # 2 3
    N //= K # 5 1
    print("N :" , N)

count += (N - 1)

print("count : " , count)



  