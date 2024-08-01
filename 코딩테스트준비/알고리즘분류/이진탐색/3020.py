import sys

def binary_search(data_list, target) :
    left = 0
    right = len(data_list) - 1  #2
    while left <= right :
          mid = (left + right) // 2
          if data_list[mid] <= target :
               left = mid + 1
          else :
               right = mid - 1
    print(right)
    return len(data_list) - (right + 1)

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

ans = n
cnt = 0

for i in range(1, h+1) :
     down_num = binary_search(bottom_arr, i-1)
     if(i == 1) :
          print("down : " , down_num)
     up_num = binary_search(top_arr, h-i)
     cur_num = down_num + up_num
     if cur_num < ans :
          ans = cur_num
          cnt = 1
     elif cur_num == ans:
          cnt += 1

print(ans, cnt)


     
