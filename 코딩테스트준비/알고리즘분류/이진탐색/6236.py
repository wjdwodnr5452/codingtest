import sys

n, m = map(int, sys.stdin.readline().split())


def binary_search(start, end, target) :
    
    result_money = 0

    while start <= end :
        mid = (start + end) // 2
        money = mid

        count = 1

        for i in money_arr :
            if(money < i) :
                money = mid
                count += 1
            money -= i

        if target < count or mid < max(money_arr) :
            start = mid + 1
        else :
            end = mid - 1
            result_money = mid

    return result_money
        

money_arr = []

for i in range(n) :
    money_arr.append(int(sys.stdin.readline()))

min_money = min(money_arr)
max_money = sum(money_arr)    

result = binary_search(min_money, max_money, m)

print(result)