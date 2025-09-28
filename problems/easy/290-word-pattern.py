class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_arr = s.split(' ')

        if len(s_arr) != len(pattern):
            return False

        s_map = {}
        p_map = {}

        for i in range(len(pattern)):
            if s_arr[i] not in s_map:
                s_map[s_arr[i]] = i 
            if pattern[i] not in p_map:
                p_map[pattern[i]] = i
                
            if p_map[pattern[i]] != s_map[s_arr[i]]:
                return False
            
        return True
                
        
        