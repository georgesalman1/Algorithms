def GradientDescent(arr):
    Minimas = []
    max_index = arr.index(max(arr))
    Right = max_index
    Left = max_index
    while 1:
        if Left-1<0 and Right+1>=len(arr):
            break
        if Left-1>=0:
            if arr[Left]<=arr[Left+1] and arr[Left]<=arr[Left-1]:
                Minimas.append(arr[Left])
            Left = Left-1
        else: 
            continue
        if Right<len(arr)-1:
            if arr[Right]<=arr[Right+1] and arr[Right]<=arr[Right-1]:
                 Minimas.append(arr[Right])
            Right = Right+1
    return Minimas
        



print(GradientDescent([4,2,7,1,5,4,2,3,8,6,4,5,3,4]))           

        
