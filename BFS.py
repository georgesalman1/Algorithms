G = [[1,2],[1,4],[4,7],[5,6],[3,4],[4,5],[5,6],[1,6]]
V = [1,2,3,4,5,6,7]
Visited = len(V)*[False]
print(Visited)

def pop_from_left(Q):
    new_queue = Q[1:len(Q)]
    return new_queue
            


    return new_queue
def neighbors(G,v):
    Neighbors = []
    for x in G:
        if x[0] == v:
           Neighbors.append(x[1])
    return Neighbors  


def BFS_CONNECTED_COMPONENT(G,u,V):
    S = []
    Visited = (len(V)+1)*[False]
    Q = [u]
    Visited[u] = True
    while len(Q) != 0:
        v = Q[0]
        print(v)
        Q = pop_from_left(Q)
        for x in neighbors(G,v):
            if not Visited[x]:
                Q.append(x)
                Visited[x] = True
        S.append(v)
    return S

def BFS_PATH(G,u,V):
    S = []
    Parent = (len(V)+1)*[0]
    Dist = (len(V)+1)*[0]
    Visited = (len(V)+1)*[False]
    Q = [u]
    Parent[u] = None
    Visited[u] = True
    while len(Q)!=0:
        v = Q[0]
        print(v)
        Q = pop_from_left(Q)
        for x in neighbors(G,v):
            if not Visited[x]:
                Q.append(x)
                Visited[x] = True
                if v==u:
                    Dist[x] = 1
                    Parent[x] = v
                else:
                    Parent[x] = v
                    Dist[x]  = 1 + Dist[Parent[x]]
        S.append(v)
    return Dist

print(BFS_CONNECTED_COMPONENT(G,3,V))
print(BFS_PATH(G,1,V))
