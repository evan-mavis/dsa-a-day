def minStartValue(self, nums: List[int]) -> int:
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
    if prefix[-1] < 0:
        return -prefix[-1]  

    return 1

