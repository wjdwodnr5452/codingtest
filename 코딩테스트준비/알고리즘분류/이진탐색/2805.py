import sys

n, m = map(int, sys.stdin.readline().split())

def binary_search(start, end) :
    result = 0

    while start <= end :
        count = 0
        mid = (start + end) // 2
        for i in arr : 
            if (i >= mid) :
                count += i - mid
        if(count >= m) : 
            result = mid
            start = mid + 1
        else : 
            end = mid - 1
    return result

arr = list(map(int, sys.stdin.readline().split()))

arr.sort()


result = binary_search(1, arr[-1])

print(result)