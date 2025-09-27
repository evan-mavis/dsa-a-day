class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        hm = {}
        for i in range(len(nums)):
            hm[nums[i]] = hm.get(nums[i], 0) + 1
        
        sum = 0
        for key, value in hm.items():    
            if value == 1:
                sum += key
            
        return sum
