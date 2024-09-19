import sys


def binary_search(start, end) :
    
    result = 0

    while start <= end : 
        
        mid = (start + end) // 2

        count = 0

        for i in arr :
            if(i > mid) :
                count += i - mid
        if(count >= m) :
            start = mid + 1
            result = mid
        else:
            end = mid - 1 
    return result     

n, m = map(int,sys.stdin.readline().split())


arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

print(binary_search(1, arr[-1]))






