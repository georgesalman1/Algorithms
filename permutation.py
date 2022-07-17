res = []
def dfs(arr, solution, visited):
    if len(solution)==len(arr):
        print(solution)
        k = []
        for i in range(len(solution)):
            k.append(solution[i])
        res.append(k)
        return
    for i in range(len(arr)):
        if visited[i]==0:  
           visited[i] = 1
           solution.append(arr[i])
           dfs(arr, solution, visited)
           solution.pop()
           visited[i] = 0


def permutation(arr):
    solution = []
    res = []
    visited = [0]*len(arr)
    dfs(arr,solution, visited)
    return res

   
arr = [1,4]
print(permutation(arr))
print(res)


        
        