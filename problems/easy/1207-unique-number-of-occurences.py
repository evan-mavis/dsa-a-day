class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hm = {}
        for i in range(len(arr)):
            hm[arr[i]] = hm.get(arr[i], 0) + 1 

        freq_set = set()
        for freq in hm.values():
            if freq in freq_set:
                return False

            freq_set.add(freq)
            
        return True

