import sys

# 테스트 케이스 횟수
num = int(sys.stdin.readline())


# 지원자 점수 
compuny_arr = []

# 테스트 케이스 만큼 실행
for i in range(num) :
    # 지원자 수
    compuny_num = int(sys.stdin.readline()) 
    for j in range(compuny_num) :
        # 지원자 점수 
        score1, score2 = map(int, sys.stdin.readline().split())
        score_arr = []
        score_arr.append(score1)
        score_arr.append(score2)
        compuny_arr.append(score_arr)
    
    compuny_arr.sort()
    
    top = 0
    result = 1

    for i in range(1, len(compuny_arr)):
        if(compuny_arr[i][1] <= compuny_arr[top][1]) :
            result += 1
            top = i

    print(result)
    compuny_arr = []
   




        



