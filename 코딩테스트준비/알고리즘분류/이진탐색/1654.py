import sys

k, n = map(int, sys.stdin.readline().split())

def binary_search(array, target, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        count = sum(x // mid for x in array)
        
        if count >= target:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result

arr = []

for _ in range(k):
    arr.append(int(sys.stdin.readline()))

# 시작값은 1, 끝값은 배열 중 가장 큰 값으로 설정
result = binary_search(arr, n, 1, max(arr))

print(result)