# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next




def merge_two_linkedlist(L1,L2):
    ptr1 = L1
    ptr2 = L2
    dummy = ListNode(-1)
    new_list = dummy
    while(1):
        if ptr1 == None and ptr2 == None:
            break
        if ptr1 == None and ptr2!= None:
            new_list.next = ListNode(ptr2.val)
            ptr2 = ptr2.next
            new_list = new_list.next
            continue
        if ptr1 != None and ptr2== None:
            new_list.next = ListNode(ptr1.val)
            ptr1 = ptr1.next
            new_list = new_list.next
            continue
        if ptr1.val > ptr2.val:
            new_list.next = ListNode(ptr2.val)
            ptr2 = ptr2.next
            new_list = new_list.next
        else:
            new_list.next = ListNode(ptr1.val)
            ptr1 = ptr1.next
            new_list = new_list.next
    return dummy.next



def merge_k_list(L, k):  
    if len(L)==1:
        return L[0]
    if len(L)==0:
        L = [[]]
        return L[0]
    if k>1:
        counter = (k//2)
    else:
        counter = (k//2)+1
    while(counter!=0):
       merged =  merge_two_linkedlist(L[0], L[1])
       L.pop(0)
       L.pop(0)
       counter = counter - 1
       L.append(merged)
    merge_k_list(L, k/2)



list1 = ListNode(1)
ptr1 = list1
ptr1.next = ListNode(4)
ptr1 = ptr1.next
ptr1.next = ListNode(5)



list2 = ListNode(1)
ptr2 = list2
ptr2.next = ListNode(3)
ptr2 = ptr2.next
ptr2.next = ListNode(4)


list3 = ListNode(2)
ptr3 = list3
ptr3.next = ListNode(6)
      

L = []
merge_k_list(L,3)

g = L[0]

x= 5