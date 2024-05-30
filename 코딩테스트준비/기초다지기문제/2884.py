clock = list(map(int, input().split()))

# 시
h = clock[0]

# 분
m = clock[1]

# 45분 보다 클 경우
if(m >= 45) :
    print(h)
    print(m - 45)
else :
    if(h == 0):
        h = 23
    else :
        h = h-1
    print(h)        
    print(m + 15)


