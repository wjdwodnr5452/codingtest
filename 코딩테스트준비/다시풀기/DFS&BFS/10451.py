import sys
sys.setrecursionlimit(10**6)

def dfs(start, arr, check) :
    
    check[start] = True

    arr_num = arr[start]

    if(check[arr_num] == False) :
        dfs(arr_num, arr, check)
        
    return 1



check_arr = []
graph = []



t = int(sys.stdin.readline())

for i in range(t) :

    n = int(sys.stdin.readline())

    graph = list(map(int, sys.stdin.readline().split()))
    graph.insert(0,0)
    check_arr = [False for _ in range(n+1)]

    result = 0

    for i in range(1, n+1) : 
        if(check_arr[i] == False) :
            result += dfs(i, graph, check_arr)

    print(result)
        

