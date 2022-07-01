# Definition for singly-linked list.
    



def merge_two_list(L1,L2):
    L = []
    ptr1 = 0
    ptr2 = 0
    while (1):
        if ptr1>=len(L1) and ptr2>=len(L2):
            break
        if ptr1>=len(L1) and ptr2<len(L2):
            L.append(L2[ptr2])
            ptr2 = ptr2 +1
            continue
        if ptr1<len(L1) and ptr2>=len(L2):
            L.append(L1[ptr1])
            ptr1 = ptr1 +1
            continue
        if L1[ptr1]> L2[ptr2]:
           L.append(L2[ptr2])
           ptr2 = ptr2 +1 
        else:
           L.append(L1[ptr1])
           ptr1 = ptr1 +1 
    return L

def merge_k_list(L, k):
    if k==1 or k==0:
        return L[0]
    counter = 0
    while(counter!=(k//2)):
       merged =  merge_two_list(L[0], L[1])
       L.pop(0)
       L.pop(0)
       counter = counter + 1
       L.append(merged)
    merge_k_list(L, k/2)



       
    






L1 = [1,2,6,7]
L2 = [3,7,9,11]
L3 = [3,5,6,8]
L4 = [5,5.5,8,24]



L = [[]]
length = len(L)
print(merge_k_list(L,length))





        
        

            


            
        
