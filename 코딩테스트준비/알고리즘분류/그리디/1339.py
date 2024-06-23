import sys

num = int(sys.stdin.readline())

alpabat_list = [sys.stdin.readline().strip() for _ in range(num)]

word = {}

for i in alpabat_list :

    x = len(i) - 1

    for j in i :
        if j in word: # 딕셔너리 여부 확인
            word[j] +=  10 ** x
        else : 
            word[j] = 10 ** x
        x = x-1

word_sort = sorted(word.values(), reverse=True)

cnt = 9
result = 0

for i in word_sort:
    result += int(i) * cnt
    cnt -= 1

print(result)











    

