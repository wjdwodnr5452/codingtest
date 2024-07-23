# 두 배열은 N개의 원소로 구성
# 동빈이는 최대 K번의 바꿔치기 연산 가능
# 바꿔치기 연산이란 배열 A에 있는 원소 하나와 배열 B에 있는 원소를 하나를 골라서 두 원소를 서로 바꾸는 것
# 동빈이의 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것
# N, K 그리고 배열 A와 B의 정보가 주어졌을 때, 최대 K 번의 바꿔치기 연산을 수행하여 만들 수 있는
# 배열 A의 모든 원소의 합의 최댓값을 출력하는 프로그램을 작성


import sys

n, k = map(int, sys.stdin.readline().split())

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

count = 0

indexA = 0
indexB = 0

while count < k :
    print(count)

    for i in range(len(a)) :
        if(a[indexA] > a[i]) :
            indexA = i

    for i in range(len(b)) :
        if(b[indexB] < b[i]) :
            indexB = i
    
    if(a[indexA] < b[indexB]) :
        a[indexA], b[indexB] = b[indexB], a[indexA]

    count += 1


print(a)
print(b)



