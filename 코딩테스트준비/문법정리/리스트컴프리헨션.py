# 0 ~ 9까지 반복문으로 원소 넣어주기
array = [i for i in range(10)]

print(array)


# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]

print(array)

# 1 부터 9까지의 수들의 제곱 값을 포함하는 리스트
array = [i * i for i in range(1, 20)]

print(array)