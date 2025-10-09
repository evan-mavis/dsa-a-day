"""
LIFO -> use a stack

1) create stack
2) iterate through each character in the string
3) if the character matches the top of the stack (upperCase = lowerCase character), then pop the top item off and skip appending to stack
    -> find a way a character complement
        1) through a map of all the english characters
        2) compare ascii values
4) otherwise append character to stack
5) at the end join the array into a string
"""
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
       
        for c in s:
            if stack and c.lower() == stack[-1].lower() and c != stack[-1]:
                stack.pop()
            else:
                stack.append(c)

        return "".join(stack)

                