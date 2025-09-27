class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counts = {}
        max_length = 0

        left = 0
        for right in range(len(nums)):
            counts[nums[right]] = counts.get(nums[right], 0) + 1

            while counts[nums[right]] > k:
                counts[nums[left]] -= 1

                if counts[nums[left]] == 0:
                    counts.pop(nums[left])

                left += 1
                    
            max_length = max(max_length, right - left + 1)

        return max_length

            
