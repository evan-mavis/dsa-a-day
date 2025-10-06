"""
ex:
1 -> 5 -> 2 -> 3 -> 2
1    2    3    4    5

output:
1 -> 2 -> 2 -> 5 -> 3

1) create two dummy nodes to break apart the linked list
2) first dummy will point to odd linked list
3) the second dummy will point to the even linked list
4) then we iterate through the entirety of the ll and append to this ll
5) combine the the linked lists by attaching the first ll tail to the dummy.next of the second ll
"""
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        
        # create dummy heads for odd and even lists 
        dummyOdd = ListNode(-1)
        dummyEven = ListNode(-1)
        
        # pointers for building the lists
        currOdd = dummyOdd
        currEven = dummyEven
        
        # Current pointer for iteration
        current = head
        isOdd = True
        
        while current:
            if isOdd:
                currOdd.next = current
                currOdd = currOdd.next
            else:
                currEven.next = current
                currEven = currEven.next
            
            isOdd = not isOdd
            current = current.next
        
        # Terminate the even list
        currEven.next = None
        
        # Connect odd list to even list
        currOdd.next = dummyEven.next
        
        return dummyOdd.next
        