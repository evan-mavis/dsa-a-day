# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
ex:
1 -> 2 -> 3 -> 4 -> 5
dummy -> 1 -> 2 -> 3 -> 4 -> 5
        prev

left = 2
right = 4

dummy

To reverse a LL
prev, next, curr
"""

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy 

        for _ in range(left - 1):  
            prev = prev.next

        curr = prev.next
        nextNode = None
        prevSub = prev
        subTail = curr        
        for _ in range(right - left + 1):
            nextNode = curr.next
            curr.next = prevSub
            prevSub = curr
            curr = nextNode

        prev.next = prevSub
        subTail.next = curr
        
        return dummy.next
        





