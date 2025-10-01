# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        if head.next is None:
            return True

        slow = head
        fast = head

        # finding the middle of the ll
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow # slow is the middle node
        # reversing the second half of the list
        while curr: 
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        first = head
        second = prev

        # iterate through each ll to see if they match
        while second:
            if second.val != first.val:
                return False

            first = first.next
            second = second.next

        return True