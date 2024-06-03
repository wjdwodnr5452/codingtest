num = int(input())
result = 0

if(num >= 5) :
    divied = num % 5 
    if(divied != 0 and divied % 3 == 0):
        result = num // 5
        result += divied // 3
    else : 
        if(num % 5 == 0) :
            result = num // 5
        else :
            if(num % 3 == 0):
                result = num // 3
            else :
                num -= 5
                result += 1
                result += num // 3

    print(result)
else : 
    if(num % 3 == 0):
        result = num // 3
    else :
        result = -1
    print(result)
    
# 예전 소스가 더 간결하고 정답이었음 다시 풀기








