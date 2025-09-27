class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        counts = {}
        left = 0
        max_sum = 0
        curr_sum = 0
        
        for right in range(len(nums)):
            counts[nums[right]] = counts.get(nums[right], 0) + 1
            curr_sum += nums[right]
            
            while counts[nums[right]] > 1:
                curr_sum -= nums[left]
                counts[nums[left]] -= 1
                left += 1
            
            max_sum = max(max_sum, curr_sum)
        
        return max_sum