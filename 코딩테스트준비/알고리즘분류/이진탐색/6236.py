import sys

n, m = map(int, sys.stdin.readline().split())

arr = []

def binary_search(start, end, target) :
    result = 0
    while start <= end :
        mid = (start + end) // 2
        money = money_arr[mid]
        count = 1

        for i in arr :
            if(money >= i) :
                money -= i
            else :
                count += i // money_arr[mid]
                if(i % money_arr[mid] == 0) :
                    count += 1
                    money = money_arr[mid]
                else :
                    count += 1
                    money = money_arr[mid] - (i % money_arr[mid])

        if target <= count :
            start = mid + 1 
            result = money_arr[mid]
        else :
            end = mid - 1
    return result

    
for i in range(n) : 
    arr.append(int(sys.stdin.readline()))

arr.sort()
money_arr = list(set(arr))

result = binary_search(0, len(money_arr)-1, m)

print(result)
