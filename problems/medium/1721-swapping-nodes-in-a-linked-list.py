# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
k = 2
1 -> 2 -> 3 -> 4 -> 5
"""
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head

        first = head
        for _ in range(k - 1):
            first = first.next
            
        temp = first
        last = head 
        while temp.next:
            temp = temp.next
            last = last.next 

        last.val, first.val = first.val, last.val
        
        return head
            




            









        