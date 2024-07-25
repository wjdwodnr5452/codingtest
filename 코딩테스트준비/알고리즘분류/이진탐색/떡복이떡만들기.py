# 높이 (h)를 지정하면 줄지어진 떡을 한 번에 절단한다. 높이가 h보다 긴 떡은 h 위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않습니다.
# 예를 들어 19, 14, 10, 17 cm인 떡이 나란히 있고 절단기 높이를 15cm로 지정하면 자른 뒤 떡의 높이는 15, 14, 10, 15cm가 될 것입니다. 잘린 떡의 길이는 차례대로 4, 0, 0, 2cm입니다.
# 손님은 6cm 만큼의 길이를 가져 갑니다.
# 손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하세요

import sys

def binary_search(array, target, start, end) :

    if start > end:
        return None
    
    count = 0
    
    mid = (start + end) // 2

    for i in array :
        if(array[mid] < i) :
            count +=  i - array[mid]
           
    if target == count :
        return array[mid]
    elif target < count :
        binary_search(array, target, start, mid-1)
    elif target > count :
        binary_search(array, target, start-1, mid)


# 떡의 개수, 떡의 길이
n, m = map(int, sys.stdin.readline().split())

# 떡
arr = list(map(int,sys.stdin.readline().split()))
arr.sort()

result = binary_search(arr, m, 0, len(arr)-1)

print(result)    



