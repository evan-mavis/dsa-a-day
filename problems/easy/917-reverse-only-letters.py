class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        characterList = list(s)
        r = len(characterList) - 1

        for l in range(len(characterList)):
            leftChar = characterList[l]
            rightChar = characterList[r]

            isLeftAlpha = leftChar.isalpha()
            isRightAlpha = rightChar.isalpha()

            if isLeftAlpha and isRightAlpha:
                temp = characterList[l]
                characterList[l] = characterList[r]
                characterList[r] = temp

            if not isLeftAlpha:
                l += 1
            if not isRightAlpha: 
                r -= 1

        return "".join(characterList)
