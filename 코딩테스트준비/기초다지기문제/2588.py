num = [input() for _ in range(2)] 

num1 = num[0]
num2 = num[1]

for i in reversed(range(len(num[1]))):
    print(int(num1) * int(num2[i]))


print(int(num1) * int(num2))






