class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_hm = {}
       
        for i in range(len(order)):
           order_hm[i] = order[i] 

        count_hm = {}
        for i in range(len(s)):
            count_hm[s[i]] = count_hm.get(s[i], 0) + 1

        result_arr = []
        for char in order_hm.values():
            if char in count_hm:
                while count_hm[char] > 0:
                    result_arr.append(char)
                    count_hm[char] = count_hm[char] - 1
                    if count_hm[char] < 0:
                        count_hm.pop(char)

        for char in count_hm.keys():
            while count_hm[char] > 0:
                result_arr.append(char)
                count_hm[char] = count_hm[char] - 1
                if count_hm[char] < 0:
                    count_hm.pop(char)

        return "".join(result_arr)