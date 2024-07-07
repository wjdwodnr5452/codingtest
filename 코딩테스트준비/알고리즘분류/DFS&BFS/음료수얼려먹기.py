import sys


def dfs(x,y) :
   
   print("호출 : " , x , y)

   if x <= -1 or x >= n or y <= -1 or y >= m:
       return False
   
   if ice_graph[x][y] == 0:
       # 해당 노드 방문 처리
       ice_graph[x][y] = 1
       # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
       dfs(x-1, y)
       dfs(x, y-1)
       dfs(x+1, y)
       dfs(x, y+1)
       print("true 시점 :" , x, y)
       return True
   return False


n, m = map(int, sys.stdin.readline().split())


ice_graph = []

for i in range(n) :
    ice = list(sys.stdin.readline().strip())
    ice = [int(char) for char in ice]
    ice_graph.append(ice)

# 모든 노드에 대하여 음료수 채우기
result = 0
for i in range(n) :
    for j in range(m) :
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            print("dfs : " , i , j)
            result += 1

print(result)


