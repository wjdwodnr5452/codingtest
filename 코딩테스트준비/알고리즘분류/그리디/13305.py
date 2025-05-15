import sys

n = int(sys.stdin.readline())

# 도로 길이
len_arr = list(map(int, sys.stdin.readline().split()))

# 리터
liter_arr = list(map(int, sys.stdin.readline().split()))


result = 0
target = liter_arr[0]


for i in range(len(liter_arr)-1) :
    if(i == 0) :
        result += target * len_arr[i]
    else :
        if(liter_arr[i] > target) : # 다음 리터가 클 경우
            result += target * len_arr[i]
        else :
            target = liter_arr[i]
            result += target * len_arr[i]
            
print(result)
            
            

    










