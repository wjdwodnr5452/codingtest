report = int(input())

num = int(input())
result = 0

for i in range(num):
    moneny, n = map(int, input().split())
    result += moneny * n
    
if(result == report) :
    print("Yes")
else :
    print("No")