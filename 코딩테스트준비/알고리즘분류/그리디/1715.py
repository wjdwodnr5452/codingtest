import sys

n =  int(sys.stdin.readline())

arr = []

for i in range(n) :
    arr.append(int(sys.stdin.readline()))

arr.sort()

first_num = arr[0]
result_arr = []

for j in arr[1:]:
    first_num += j # 30
    result_arr.append(first_num)

result = 0

for k in result_arr :
    result += k

print(result)

    





