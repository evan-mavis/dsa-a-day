class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hm = {}
        max_freq = 0
        
        for i in range(len(nums)):
            hm[nums[i]] = hm.get(nums[i], 0) + 1
            max_freq = max(max_freq, hm[nums[i]])
       
        max_freq_element_count = 0 
        for freq in hm.values():
            if freq == max_freq:
                max_freq_element_count += freq

        return max_freq_element_count
                
        