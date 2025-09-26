class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_chars = set()

        left = 0
        maximum_length = 0
        for right in range(len(s)):
            if s[right] not in curr_chars:
                curr_chars.add(s[right])
            else:
                while s[right] in curr_chars:
                    curr_chars.remove(s[left])
                    left += 1
                curr_chars.add(s[right])
                    
            maximum_length = max(maximum_length, right - left + 1)
        
        return maximum_length