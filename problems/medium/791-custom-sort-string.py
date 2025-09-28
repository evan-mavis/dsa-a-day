class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_count = {}
        for i in range(len(s)):
            s_count[s[i]] = s_count.get(s[i], 0) + 1

        result_arr = []
        for char in order:
            result_arr.append(char * s_count.pop(char, 0))

        for char, freq in s_count.items():
            result_arr.append(char * freq)

        return "".join(result_arr)