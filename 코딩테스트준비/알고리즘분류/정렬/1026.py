import sys

num = int(sys.stdin.readline())

num_list1 = list(map(int, sys.stdin.readline().split()))
num_list2 = list(map(int, sys.stdin.readline().split()))

num_list1.sort()

num_list2.sort(reverse=True)

result = 0

for i in range(num):
    result += num_list1[i] * num_list2[i]

print(result)


