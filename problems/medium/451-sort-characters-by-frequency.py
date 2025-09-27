class Solution:
    def frequencySort(self, s: str) -> str:
        counts = {}
        
        for c in s:
            counts[c] = counts.get(c, 0) + 1

        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

        result_arr = []
        for num, count in sorted_counts:
            for _ in range(count):
                result_arr.append(num) 

        return "".join(result_arr)

        
            

        