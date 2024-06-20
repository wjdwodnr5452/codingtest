import sys
n,m = map(int, sys.stdin.readline().split())
arr1 = []
arr2 = []

for i in range(m):
    num1, num2 = map(int, sys.stdin.readline().split())
    arr1.append(num1)
    arr2.append(num2)

money1 = min(arr1) 

result = 0
while n > 0 :
    if(n >= 6):
        money2 =  min(arr2) * 6
        n -= 6
    else :
        money2 =  min(arr2) * n
        n -= n
    if(money1 < money2) :
        result += money1
    else :
        result += money2
print(result)

