class Solution:
    def minWindow(self, s: str, t: str) -> str:

        char_map = defaultdict(int)
        for ch in t: 
            char_map[ch] += 1

        start, length, min_len = len(s), 0, len(s) + 1

        for i in range(len(s)):
            copy_map = char_map.copy()

            j = i
            length = 0
            while j < len(s): 
                if not copy_map: 
                    break
                if s[j] in copy_map: 
                    if copy_map[s[j]] > 1: 
                        copy_map[s[j]] -= 1
                    else: 
                        copy_map.pop(s[j])
                length += 1
                j += 1
            
            if not copy_map: 
                if length < min_len: 
                    start = i
                    min_len = length

        if start == len(s): 
            return ""

        return s[start:start + min_len]