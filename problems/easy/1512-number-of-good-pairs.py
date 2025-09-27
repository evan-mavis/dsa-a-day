class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hm = {}
        pairs = 0
        for i in range(len(nums)):
            if nums[i] in hm:
                pairs += hm[nums[i]] 

            hm[nums[i]] = hm.get(nums[i], 0) + 1

        return pairs

        

        