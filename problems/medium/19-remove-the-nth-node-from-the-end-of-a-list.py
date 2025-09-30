# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
-> use the fast and slow pointer technique
-> if I am deleting a node, I always should store some prev (since this is not a doubly ll)

fast will be iterated up n times  
slow will start at current
then I will have another loop that will move them at the same speed 
fast should hit the end, at this point slow should be on the deletion node
slow is one behind, and I can do that through use of a dummy node

1 -> 2
slow -> 1 -> 2 -> none
        slow      fast

"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        dummy = ListNode(0, head)
        slow = dummy
        fast = head

        for _ in range(n):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next  

        return dummy.next
