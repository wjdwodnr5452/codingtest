import sys


def binary_search(start, end) :
    
    result = 0 

    while start <= end :
        
        mid = (start +  end) // 2
        current = arr[0]
        count  = 1

        for i in arr : 
            if(i >= current + mid) :
                count += 1
                current = i
        if count >= c :
            start = mid + 1
            result = mid
        else :
            end = mid -1

    return result

n, c = map(int, sys.stdin.readline().split())

arr = []

for i in range(n) :
    arr.append(int(sys.stdin.readline()))

arr.sort()

print(binary_search(1, arr[-1]-arr[0]))

