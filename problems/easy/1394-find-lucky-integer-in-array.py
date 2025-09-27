class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hm = {}
        lucky = -1 

        recheck = False
        for i in range(len(arr)):
            hm[arr[i]] = hm.get(arr[i], 0) + 1 

            if arr[i] == hm[arr[i]]:
                lucky = max(lucky, arr[i])
            elif arr[i] < hm[arr[i]] and lucky == arr[i]:
                recheck = True
        
        lucky2 = -1
        if recheck:
            for number, freq in hm.items():
                if number == freq:
                    lucky2 = max(lucky2, number)
            return lucky2
        else:
            return lucky
                
                