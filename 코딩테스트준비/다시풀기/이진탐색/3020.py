import sys

n, h = map(int, sys.stdin.readline().split())

def h_count(hegiht, target) :
    count = 0
    for i in target :
        if(hegiht <= i) :
            count += 1
    return count


right = []
left = []

for i in range(n) :
    if(i % 2 == 0) :
        left.append(int(sys.stdin.readline()))
    else :
        right.append(int(sys.stdin.readline()))

right.sort()
left.sort()

result = n

result_count = 0

for i in range(1, h+1) :

    right_cnt = h_count(i, right)
    left_cnt = h_count((h-i)+1, left)

    if(result > right_cnt + left_cnt) :
        result = right_cnt + left_cnt
        result_count = 1
    elif(result == right_cnt + left_cnt) :
        result_count += 1


print(result, result_count)
    

    















