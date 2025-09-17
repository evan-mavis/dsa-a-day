class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0]
        
        for i in range(len(nums)):
            prefix.append(prefix[-1] + nums[i])
            
        for j in range(1, len(prefix)):
            if prefix[j - 1] == (prefix[-1] - prefix[j]):
                return j - 1

        return -1
        