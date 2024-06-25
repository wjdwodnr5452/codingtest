import sys

bingo_pan = [sys.stdin.readline().strip().split() for _ in range(5)] 

bingo_value = [sys.stdin.readline().strip().split() for _ in range(5)] 

check_pan = [[0,0,0,0,0] for _ in range(5)]

count = 0

def bingo_search(value) :
    for i in range(len(bingo_pan)) :
        for j in range(len(bingo_pan[i])) :
            if(bingo_pan[i][j] == value):
                m , n = i, j
                return m, n
            
def bingo_check(m,n) :
    check_pan[m][n]
    bingo_count = 0

    # 세로
    for i in range(5) :
        count = 0 
        for j in range(5) :
            if(check_pan[i][j] == 0):
                count = 0
            else :
                count += 1  
        if(count >= 5) :
            bingo_count += 1
    
    # 가로
    for i in range(5) :
        count = 0
        for j in range(5) :
            if(check_pan[j][i] == 0):
                count = 0
            else :
                count +=1
        if(count >= 5) :
            bingo_count += 1


    # 대각선 (0,0 ~ 4,4)
    count_diagonal = 0
    for i in range(5):
        if(check_pan[i][i]) :
            count_diagonal = 0
        else :
            count_diagonal += 1
    
    if(count_diagonal >= 5) :
        bingo_count += 1
    
    # 대각선 (0,4 ~ 4,0)
    count_diagonal1 = 0
    for i in range(5) :
        if(check_pan[i][4-i]):
            count_diagonal1 = 0
        else :
            count_diagonal1 += 1

    if(count_diagonal1 >= 5) :
        bingo_count += 1

    return bingo_count


result = 0

for i in bingo_value :
    for j in i :
        m, n = (bingo_search(j))
        check_pan[m][n] = 1
        count += bingo_check(m, n)
        result += 1

        if(count >= 3):
            print("빙고 : " , result)
            break








