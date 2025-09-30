# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
fast and slow technique
slow and only move it to the next node if fast (which is one ahead) is not the same value

[1,2,3,3,4,4,5]
p [1,2,3,3,4,4,5]
   s f
     s f
     p s    f


"""
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head 

        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        curr = head
        
        while curr and curr.next:
            if curr.val == curr.next.val:
                saved_val = curr.value
                
                while curr.val == saved_val:
                    curr = curr.next
                    
                prev.next = curr
            else:
                prev = curr
                curr = curr.next

        return dummy.next
        

        