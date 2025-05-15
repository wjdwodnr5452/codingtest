import sys

def binary_search(start,end,target) :
    
    while start <= end :

        mid = (start + end) // 2 

        if(card_list[mid] <= target) :
            if(card_list[mid] == target) :
                break
            start = mid + 1
        else :
            end = mid - 1
   
    return mid


n = int(sys.stdin.readline())
 
card_list = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())

compare_list = list(map(int, sys.stdin.readline().split()))

result_list = []

card_list.sort()

for i in compare_list :
    index = binary_search(0,n-1,i)
    if(card_list[index] == i) :
        print(1, end=" ")
    else :
        print(0, end=" ") 


