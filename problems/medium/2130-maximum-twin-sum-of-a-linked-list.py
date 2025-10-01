# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
1. set pointer at the middle of the linked list using slow and fast pointers
2. reverse the second half of the list
3. iterate through both l1 and l2 at the same time, add the nodes, and compute max sum
"""
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if head is None:
            return None
        if head.next is None:
            return head.val
        if head and head.next and head.next.next is None:
            return head.val + head.next.val

        # 1. 
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow is now at the start of the second list
        # 2. 
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        head2 = prev

        # 3. 
        max_sum = 0
        while head2:
            curr_sum = head.val + head2.val
            max_sum = max(max_sum, curr_sum) 

            head = head.next
            head2 = head2.next

        return max_sum


        
        