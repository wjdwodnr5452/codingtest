import sys

# 빙고판
bingo_arr = [sys.stdin.readline().strip().split() for _ in range(5)]

# 사회자가 부르는 숫자 값
bingo_value = [sys.stdin.readline().strip().split() for _ in range(5)]

# 빙고를 체크 하는 판
bingo_check = [[0,0,0,0,0] for _ in range(5)]

# 정답
result = 0

# 빙고 index 값 가져오기
def bingo_index_check(value) :
    global result
    for i in range(len(bingo_arr)) :
        for j in range(len(bingo_arr[i])) :
            if(bingo_arr[i][j] == value) :
                return i, j


# 세로줄 
def bingo_check_y() :
    bingo = 0
    for i in range(5) :
        count = 0
        for j in range(5) :
            if(bingo_check[j][i] == 1) :
                count += 1
        if(count == 5) :
            bingo += 1
    return bingo
            
# 가로줄
def bingo_check_x() :
    bingo = 0
    for i in range(5):
        count = 0
        for j in range(5) : 
            if(bingo_check[i][j] == 1) :
                count += 1
        if(count == 5) :
            bingo += 1
    return bingo
        
# 대각선 left
def bigo_check_left() :
    bingo = 0
    # 왼쪽위 -> 오른쪽 아래 카운트
    count = 0
    # 왼쪽위 -> 오른쪽 아래
    for i in range(5) :
        if(bingo_check[i][i] == 1) :
            count += 1
    if(count == 5) :
        bingo += 1
    return bingo


# 대각선 right
def bing_check_right() :
    bingo = 0
    # 오른쪽 위 -> 왼쪽 아래
    count = 0
    for i in range(5) :
        if(bingo_check[i][4-i] == 1) : 
            count += 1
    if(count == 5) :
        bingo += 1
    return bingo



# 사회자 부른 값을 빙고판 위치 가져오기
count = 0
for i in bingo_value :
    for j in i :
        # 인덱스 정보 가져오기
        y, x = bingo_index_check(j)
        # 해당 인덱스에 표시
        bingo_check[y][x] = 1
        if(bingo_check_y() == 1) :
            count += 1
        if(bingo_check_x() == 1) :
            count += 1
        if(bigo_check_left() == 1) :
            count += 1
        if(bing_check_right() == 1) :
            count += 1
        result += 1
        if(count >= 3) :
            break


print(result)        

