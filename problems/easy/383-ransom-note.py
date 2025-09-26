class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hm = {}
        for c in magazine:
            hm[c] = hm.get(c, 0) + 1
            
        for c in ransomNote:
            if hm.get(c, 0) == 0:      
                return False
            hm[c] -= 1
            
        return True