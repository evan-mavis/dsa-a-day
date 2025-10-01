# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
1. outer loop that loops through all nodes
2. inner loop determines size of group based on grouped_size variable
3. if length is even, then reverse with helper method
"""
class Solution:
    def reverse(self, head, k):
        prev = None
        curr = head
        new_tail = head

        for i in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        new_head = prev

        return new_head, new_tail, curr

    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head

        group_size = 1 
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        prev = dummy

        while curr:
            actual_group_size = 0
            temp = curr
            while temp and actual_group_size < group_size:
                temp = temp.next
                actual_group_size += 1 

            if actual_group_size % 2 == 0:
                new_head, new_tail, new_curr = self.reverse(curr, actual_group_size)
                prev.next = new_head
                new_tail.next = new_curr
                curr = new_curr
                prev = new_tail
            else:
                for _ in range(actual_group_size):
                    prev = curr
                    curr = curr.next

            group_size += 1

        return dummy.next
            
        

        