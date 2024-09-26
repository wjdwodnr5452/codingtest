n, h = map(int, input().split())

top_arr = [] # 종유석
bottom_arr = [] # 석순


# 종유석 구하기 첫번째 (7 - 1 + 1) 두번째 (7 - 2 + 1)

def binary_search(arr, target) :
    bottom = 0
    top = len(arr) - 1

    while bottom <= top :
        mid = (bottom + top) // mid
        arr[mid] 
        if(arr[mid] <= target) :
            bottom = mid +1
        else :
            bottom = mid - 1 

    
    


for i in range(n) :
    if (i % 2 == 0) :
        top_arr.append(int(input()))
    else :
        bottom_arr.append(int(input()))

top_arr.sort()
bottom_arr.sort()


for i in range(h+1) :
    bottom_height = i+1
    top_height = (h-i)+1

    bottom_cnt = binary_search(bottom_arr, bottom_height)
    top_cnt = binary_search(top_arr, top_height)



#binary_search(1, h)




        


