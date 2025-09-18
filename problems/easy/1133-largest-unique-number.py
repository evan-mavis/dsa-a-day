class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        hash_map = {}
        
        for i in range(len(nums)):
            hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1
        
        max_value = -1
        for k, v in hash_map.items():
            if k > max_value and v == 1:
                max_value = k
                
        return max_value