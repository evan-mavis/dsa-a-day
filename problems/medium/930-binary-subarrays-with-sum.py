class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_count = {0: 1}  
        current_sum = 0
        result = 0
        
        for num in nums:
            current_sum += num  
            
            if current_sum - goal in prefix_count:
                result += prefix_count[current_sum - goal]
            
            prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1
        
        return result