# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
I want 4 things here to redo the connections
-> beforeReverseNode
-> afterReverseNode
-> firstReverseNode
-> lastReverseNode

1 -> 2 -> 3 -> 4 -> 5
"""
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        beforeReverseNode = None
        afterReverseNode = None
        firstReverseNode = None
        lastReverseNode = None

        currCount = 1
        curr = head

        while currCount < left:
            beforeReverseNode = curr
            curr = curr.next 
            currCount += 1  
        firstReverseNode = curr

        while currCount < right:
            curr = curr.next
            currCount += 1 
        lastReverseNode = curr
        afterReverseNode = curr.next

        # Reverse the segment
        prev = None
        curr = firstReverseNode
        for _ in range(right - left + 1):
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        # Reconnect the pieces
        if beforeReverseNode:
            beforeReverseNode.next = lastReverseNode
        else:
            head = lastReverseNode

        firstReverseNode.next = afterReverseNode

        return head

