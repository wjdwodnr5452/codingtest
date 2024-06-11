import sys
from collections import Counter

num = int(sys.stdin.readline())

num_arr = []

for i in range(num):
    num_arr.append(int(sys.stdin.readline()))

num_arr.sort()

#################################

# 산술평균값 구하기
result1 = 0

for i in num_arr:
    result1 += i

result1 = result1 / num

# 산술평균
print(round(result1))

##################################

# 중앙값
mid = num // 2 
if(len(num_arr) == 1):
    print(num_arr[0])
else :
    print(num_arr[mid])


#################################

# 최빈값 
count_item = Counter(num_arr)
max_item = count_item.most_common(n=2)

if(len(max_item) > 1) :
    if(max_item[0][1] == max_item[1][1]):
        print(max_item[1][0])
    else :
        print(max_item[0][0])
else :
    print(max_item[0][0])


#################################
# 범위
print(max(num_arr) - min(num_arr))