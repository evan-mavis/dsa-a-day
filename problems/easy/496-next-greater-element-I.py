"""
ex:
nums2 -> [5, 3, 6, 1 ,2]
nums1 -> [3, 6]

stack
3 5
"""
class Solution:
   def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hm = {}
        decreasing = []
        for num in nums2:
            while decreasing and num > decreasing[-1]:
                hm[decreasing.pop()] = num

            decreasing.append(num)
            
        for num in nums2:
            if num not in hm:
                hm[num] = -1
                
        ans = []
        for num in nums1:
            ans.append(hm[num])
            
        return ans
        