class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        ans = 0
        temp = 0

        # another random change here

        for i in range(k):
            if s[i] in vowels:
                temp += 1
                ans = max(ans, temp)

        left = 0
        for right in range(k, len(s)):
            if s[right] in vowels:
                temp += 1
            
            right += 1
            if s[left] in vowels:
                temp -= 1
            left += 1

            ans = max(ans, temp)

            if ans == k:
                return ans

        return ans
            

                
