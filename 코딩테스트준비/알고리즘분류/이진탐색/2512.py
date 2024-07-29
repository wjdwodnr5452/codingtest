import sys

def binary_search(start, end) :

    result = 0
    
    while start <= end :
        
        count = 0
        
        mid = (start + end) // 2

        for i in arr :
            if(i > mid) :
                count += mid
            else :
                count += i

        if (count <= m) :
            start = mid + 1
            result = mid
        else :
            end = mid - 1
    
    return result


n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())

arr.sort()

result = binary_search(1, arr[-1])

print(result)
