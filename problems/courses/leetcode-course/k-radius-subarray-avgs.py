def getAverages(self, nums: List[int], k: int) -> List[int]:
    prefix = [nums[0]]
    
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
        
    ans = []
    denom = k + k + 1
    for j in range(0, len(nums)):
        if j - k < 0 or j + k > len(nums) - 1:
            ans.append(-1)
        else:
            range_start_idx = j - k
            range_end_idx = j + k 
            sum = prefix[range_end_idx] - prefix[range_start_idx] + nums[range_start_idx]
            avg = int(sum / denom)
            ans.append(avg)
            
    return ans