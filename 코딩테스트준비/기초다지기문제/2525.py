# 시 분
h, m = map(int, input().split())
# 더할 숫자
add = int(input())

# 분 더하기
m_sum = m + add

if(m_sum >= 60):
    # 시 더하기
    h_add = m_sum // 60
    h_sum = h + h_add
    if(h_sum == 24) :
        print(0)
    elif(h_sum > 24) :
        print(h_sum - 24)
    elif(h_sum < 24) :
        print(h_sum)

    if(m_sum % 60 == 0):
        print(0)
    else :
        print(m_sum - (60 * h_add))
else :
    print(h)
    print(m_sum)



