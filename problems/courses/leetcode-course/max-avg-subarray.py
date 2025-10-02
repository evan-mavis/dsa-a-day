def findMaxAverage(nums: List[int], k: int) -> float:
    sum = 0

    for j in range(k):
        sum += nums[j]

    avg = sum / k

    for i in range(k, len(nums)):
        sum += nums[i]
        sum -= nums[i - k]

        avg = max(avg, sum / k) 

    return avg
