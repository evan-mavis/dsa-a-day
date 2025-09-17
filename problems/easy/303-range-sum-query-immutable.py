class NumArray:
    def __init__(self, nums: List[int]):
        l = len(nums)
        self.prefix = [0] * l
        prev = 0
        for i in range(l):
            prev = prev + nums[i]
            self.prefix[i] = prev

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left-1]