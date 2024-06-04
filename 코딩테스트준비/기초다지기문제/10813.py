# 바구니 갯수, 바꾸는 갯수
m, n = map(int, input().split())

# 바구니
list = []

# 바구니 순서
for i in range(m) :
    list.append(i+1)

for i in range(n) :
    index1, index2 = map(int, input().split()) # 바구니 변경 위치
    list[index1-1], list[index2-1] = list[index2-1], list[index1-1]

print(*list)





    
    

