# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
lets iterate through he linked list normally
I want to create a helper method to delete node
-> I keep track of a previous pointer to remove it so we can keep the ll connected

1. define a prev and current to iterate through the loop
2. create while loop
3. create helper method to delete node
-> may not be needed
4. return the head of the list
5. make sure to keep a dummy just in case head gets deleted

# val = 5
5 -> 2 -> 3 -> 5 -> 6 
"""
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        prev = dummy

        curr = head
        while curr:
            if curr.val == val:
                prev.next = curr.next

            prev = curr              
            curr = curr.next

        return dummy.next
        