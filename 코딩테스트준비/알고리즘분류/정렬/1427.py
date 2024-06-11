import sys

num_str = sys.stdin.readline().strip()

num_arr = []

for i in num_str :
    num_arr.append(int(i))

num_arr.sort(reverse=True)

result = ""

for i in num_arr:
    result+= str(i)

print(result)

 