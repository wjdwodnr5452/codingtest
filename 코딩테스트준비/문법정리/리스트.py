
import sys

a = [1,2,3,4,5,6,7,8,9]
#print(a)

# 네 번째 원소만 출력
#print(a[3])


# 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n
#print(a)


N = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

print(arr)

