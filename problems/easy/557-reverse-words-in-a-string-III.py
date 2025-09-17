class Solution:
    def reverseWords(self, s: str) -> str:
        arr = list(s)
        left = 0

        for i in range(len(arr)):
            if arr[i] == " ":
                right = i - 1
                while left <= right:
                    arr[left], arr[right] = arr[right], arr[left]
                    left += 1
                    right -= 1
                left = i + 1
            elif i == len(arr) - 1:
                right = i
                while left <= right:
                    arr[left], arr[right] = arr[right], arr[left]
                    left += 1
                    right -= 1

        return "".join(arr)
        