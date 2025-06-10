#  1. 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
#  2. 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
#  3. 마지막 도착 계단은 반드시 밟아야 한다.

n = int(input())

d = [0] * 300

arr = []

for i in range(n) :
    arr.append(int(input()))

d[0] = arr[0]
d[1] = arr[1]


for i in range(2, n) :
    print(i)
    n1 = (d[i-2] + arr[i])
    print("n1 : " , n1)
    n2 = (d[i-1] + arr[i])
    print("n2 : " , n2)
    num = max(n1, n2)
    d[i] = num

#print(d[n])

