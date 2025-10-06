class solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        result = 0
        
        current = head
        while current:
            result = (result << 1) | current.val
            current = current.next
            
        return result