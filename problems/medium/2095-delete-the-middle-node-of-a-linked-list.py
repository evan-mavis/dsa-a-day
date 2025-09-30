# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
-> slow and fast pointers technique
-> also track a prev to the slow bc this is not a doubly linked list and we need the prev to connect

1 -> 2 -> 3 -> 4 -> 5
"""
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        slow = head
        fast = head
        dummy = ListNode(0, head)
        prev = dummy

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next
        slow.next = None
        
        return head