# from collections import defaultdict

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         s_map = defaultdict(int)
#         t_map = defaultdict(int)
#         for ch in s: 
#             s_map[ch] +=1
#         for ch in t: 
#             t_map[ch] +=1
#         return (s_map == t_map)

from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = defaultdict(int)
        if len(s) != len(t):
            return False
        for ch in s: 
            s_map[ch] +=1
        for ch in t: 
            s_map[ch] -=1
            if s_map[ch] < 0:
                return False
        return (sum(s_map.values()) == 0)