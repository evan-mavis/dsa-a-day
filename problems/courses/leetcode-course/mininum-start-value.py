def minStartValue(self, nums: List[int]) -> int:
        minValue = 0
        total = 0

        for num in nums:
            total += num
            minValue = min(total, minValue)
        
        return 1 - minValue

