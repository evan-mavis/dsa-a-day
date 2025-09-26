class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        curr = 0 
        hm = {}
        if number == 0:    
            curr -= 1
            hm[curr] = 0
        else:
            curr += 1
            hm[curr] = 0
        
        
        max_length = 0
        for i in range(1, len(nums)):
            if number == 0:    
                curr -= 1
            else:
                curr += 1
            
            if curr in hm:
                max_length = max(max_length, i - hm[curr])
            else:
                hm[curr] = i
                
        return max_length