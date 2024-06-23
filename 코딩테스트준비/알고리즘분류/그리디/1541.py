import sys


str = sys.stdin.readline().rstrip()

arr = str.split("-")
arr2 = []

for i in arr :
        cnt = 0
        for j in i.split("+") :
                cnt += int(j)
        arr2.append(cnt)

result = arr2[0]

if(len(arr2) > 1) :
        for i in arr2[1:] :
                result -= i

print(result)
