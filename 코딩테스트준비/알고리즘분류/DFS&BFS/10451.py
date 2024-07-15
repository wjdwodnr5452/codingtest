import sys

n = int(sys.stdin.readline())


def dfs(p) :
    if not graph_check[p] :
        graph_check[p] = True

    for i in graph[p] :
        if not graph_check[i] :
            dfs(i)


for i in range(n) :
    m = int(sys.stdin.readline())
    
    arr = list(map(int, sys.stdin.readline().split()))  
    arr.insert(0, 0)

    max_num = max(arr)

    graph = []
    graph_check = [False for _ in range(max_num+1)]
   
    for j in range(max_num+1) : 
        graph.append([j, arr[j]])

    count = 0

    for k in range(1,len(graph)) :
        if not graph_check[k] :
            count += 1
            dfs(k)
            
    print(count)

