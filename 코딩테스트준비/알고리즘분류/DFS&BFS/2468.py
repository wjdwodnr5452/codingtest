import sys

n = int(sys.stdin.readline())

graph = []

check_graph = [[False for _ in range(n)] for _ in range(n)]

max_num = 0

result = 0

def dfs(num, v) :
    print()



for i in range(n) :
    m = list(map(int, sys.stdin.readline().split()))
    if(max(m) > max_num) :
        max_num = max(m)
    graph.append(m)

for i in range(max_num) :
    for j in range(n) :
        dfs_num = dfs(i, j)
        if(dfs_num > result) :
            result = dfs_num

print(graph)