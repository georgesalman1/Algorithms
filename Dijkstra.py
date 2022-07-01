import sys
size = 0
maxsize = 200
FRONT = 0

def create(size):
        arr = []
        for i in range(size):
            arr.append([66666666666]*2)
        return arr

def parent(pos):
		return pos//2

	# Function to return the position of
	# the left child for the node currently
	# at pos
def leftChild(pos):
		return 2 * pos

	# Function to return the position of
	# the right child for the node currently
	# at pos
def rightChild(pos):
		return (2 * pos) + 1

	# Function that returns true if the passed
	# node is a leaf node
def isLeaf(pos): 
        global size
        return pos*2 > size

	# Function to swap two nodes of the heap
def swap(Heap, fpos, spos):
        Heap[fpos], Heap[spos] = Heap[spos], Heap[fpos]

    
def insert(Heap, element):
    global size
    global maxsize
    if size >= maxsize:
                return
    size =size+1 #size is more 1
    Heap[size] = element
    current = size
    while Heap[current][1] < Heap[parent(current)][1]:
       swap(Heap, current, parent(current))
       current = parent(current)
 


	# Function to heapify the node at pos
def minHeapify(Heap, pos):

		# If the node is a non-leaf node and greater
		# than any of its child
		if not isLeaf(pos):
			if (Heap[pos][1] > Heap[leftChild(pos)][1] or
			Heap[pos][1] > Heap[rightChild(pos)][1]):

				# Swap with the left child and heapify
				# the left child
				if Heap[leftChild(pos)][1] < Heap[rightChild(pos)][1]:
					swap(Heap, pos, leftChild(pos))
					minHeapify(Heap,leftChild(pos))

				# Swap with the right child and heapify
				# the right child
				else:
					swap(Heap, pos, rightChild(pos))
					minHeapify(Heap, rightChild(pos))





def minHeap(Heap):
    global size
    length = size
    for pos in range(length//2, 0, -1):
        minHeapify(Heap, pos)
    return Heap

def remove(Heap):
    global FRONT
    global size
    popped = Heap[FRONT]
    Heap[FRONT] = Heap[size]
    size = size-1
    minHeapify(Heap, FRONT)
    return popped

def neighbors(G,v):
    Neighbors = []
    for x in G:
        if x[0] == v:
           Neighbors.append(x[1])
    return Neighbors  


def vertice_in_heap(H,x):
    for element in H:
        if element[0] == x:
            return True
    return False
    

Heap = create(300)
# create heap with 300 elements
Heap1 = minHeap(Heap)





G = [[0,1,4],[0,7,8],[7,6,1],[7,8,7],[1,2,8],[1,7,11],
[6,5,2],[6,8,6],[8,2,2],[2,3,7],[3,4,9],[5,4,10],[2,8,2]]

V = [0,1,2,3,4,5,6,7,8,9,10,11]
Parent = (len(V)+1)*[0]
Dist = (len(V)+1)*[0]

source1 = 0
insert(Heap, [source1,0])

def weight(u,x):
    global G
    for element in G:
        if u == element[0] and x == element[1]:
            return element[2]
    return 6666666666
        

def dijkstra(G,u):
    global Parent
    global Dist
    global V
    for x in V:
        Dist[x] = 6666666666
        Parent[x] = None
    Dist[u] = 0
    # start heap which contain source vertex, and order in min heap by x.d while inserting in loop
    H = minHeap(Heap)
    while size != 0:
        global size
        popped = remove(H)
        v = popped[0]
        for x in neighbors(G,v):
            if Dist[v] + weight(v,x) < Dist[x]:
                Dist[x] = Dist[v] + weight(v,x)
                Parent[x]  = v
                insert(H, [x, Dist[x]])
                H = minHeap(H)
    return Dist    

#source vertex is 2
print(dijkstra(G,0))


