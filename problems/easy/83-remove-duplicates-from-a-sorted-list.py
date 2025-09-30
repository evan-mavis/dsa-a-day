# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Two pointers
ahead
behind

if
check is behind == ahead

behind.next points to ahead.next
temp = ahead
ahead = ahead.next
temp.next = None

else
increment both ahead and behind
"""

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head

        behind = head 
        ahead = head.next

        while ahead:
            if behind.val == ahead.val:
                behind.next = ahead.next
                temp = ahead
                ahead = ahead.next
                temp.next = None
            else:
                behind = behind.next
                ahead = ahead.next
        
        return head