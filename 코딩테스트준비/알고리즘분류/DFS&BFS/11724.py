import sys

sys.setrecursionlimit(10**7)
n, m = map(int, sys.stdin.readline().split())

def dfs(v) :
    check_graph[v] = True
    for i in graph[v] :
        if not check_graph[i] :
            dfs(i)
    return 1
        
# 그래프 생성
graph = [[] for _ in range(n+1)]

# 체크
check_graph = [False for _ in range(n+1)]

# 두개 연결점 받기
for i in range(m) :
    u,v = list(map(int, sys.stdin.readline().split()))

    # 받은 연결점 그래프에 넣기
    graph[u].append(v)
    graph[v].append(u)

result = 0

for i in range(1, n+1):
    if not check_graph[i] :
            result += dfs(i)
       
print(result)
            


    

