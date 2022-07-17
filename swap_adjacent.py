class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

         
def swapPairs(head):
       dummy = ListNode(0,head)
       prev, curr = dummy, head
       while curr and curr.next:
           nxtPair = curr.next.next
           second  = curr.next
           second.next = curr
           curr.next = nxtPair
           prev.next = second
           prev = curr
           curr = nxtPair
       return dummy



Head = ListNode(1)

head = Head
head.next = ListNode(3)
head = head.next
head.next = ListNode(9)
swapPairs(head)

