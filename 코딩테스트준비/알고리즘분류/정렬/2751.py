import sys

# 반복 횟수
num = int(input())

# 배열 담기기
arr = []

# 반복문
for i in range(num):
    arr.append(int(sys.stdin.readline()))

arr.sort()

for i in arr:
    print(i)