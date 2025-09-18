class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hash_map = {}
        balloon_set = set("balloon")
        
        for c in text:
            if c in balloon_set:
                hash_map[c] = hash_map.get(c, 0) + 1
            
        hash_map['l'] = hash_map.get('l', 0) / 2
        hash_map['o'] = hash_map.get('o', 0) / 2
        
        if not all(c in hash_map for c in "ballon"):
            return 0
        
        return int(min(hash_map.values()))

# cleaner solution
# class Solution:
#     def maxNumberOfBalloons(self, text: str) -> int:
#         # init HashMap (mp)
#         text = text.lower()
#         mp: dict = {}
#         mp["b"] = 0
#         mp["a"] = 0
#         mp["l"] = 0
#         mp["o"] = 0
#         mp["n"] = 0
        
#         # declare HashMap
#         for txt in text:
#             if txt in mp:
#                 mp[txt] += 1
        
#         # return min -> bottleneck
#         return min(mp["b"], mp["a"], mp["l"]//2, mp["o"]//2, mp["n"])