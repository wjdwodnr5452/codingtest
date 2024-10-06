# n 주전자 수 k 친구 수
n, k = map(int, input().split())

def binary_search(start, end) : 
    
    result = 0

    while start <= end :
        mid = (start + end) // 2

        # 주전자 나누기 
        n_count = 0 

        for i in n_arr : 
            n_count += i // mid
        
        if(n_count >= k) :
            start = mid + 1
            result = mid
        else :
            end = mid -1
            
    return result
           

# 주전자 배열
n_arr = []


for i in range(n) : 
    n_arr.append(int(input()))


n_arr.sort()

print(binary_search(1, n_arr[-1]))
