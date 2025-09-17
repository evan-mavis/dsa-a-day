class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        chars = list(word)
        right = 0
        
        has_no_matching_char = True
        while right < len(chars):
            if chars[right] == ch:
                has_no_matching_char = False
                break
            else:
                right += 1
        
        if has_no_matching_char:
            return word

        left = 0
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

        return "".join(chars)