class Solution:
    def minWindow(self, s: str, t: str) -> str:

        char_map = {}
        for ch in t: 
            char_map[ch] = char_map.get(ch, 0) + 1

        need = len(char_map)
        start, end = 0, 0
        final_start = len(s) + 1
        min_len = len(s) + 1 
        copy_map = {}

        while end < len(s):
            print("top of loop end is ", end)
            ch = s[end]

            if ch in char_map: 
                copy_map[ch] = copy_map.get(ch, 0) + 1
                if char_map[ch] == copy_map[ch]:
                    need -= 1
                    print("found a match in ending char ", ch, ", updating need to ", need)
                    if need == 0:
                        # min_len = min(min_len, end - start + 1)
                        if end - start + 1 < min_len: 
                            min_len = end - start + 1
                            final_start = start
                            print('final start has been updated to ', final_start, ' as need is now 0')
                        while start < end:
                            print("top of inner loop start is ", start)
                            ch2 = s[start]
                            if ch2 in copy_map: 
                                copy_map[ch2] -= 1
                                if char_map[ch2] != copy_map[ch2]:
                                    start += 1
                                    need += 1
                                    print("found a match in starting char ", ch2, ", updating need to ", need)
                                    break
                            start += 1
                            final_start = start
                            print('final start has been updated to ', final_start, ' as superfluos chars')
                            min_len = min(min_len, end - start + 1)


            end += 1

        if min_len == len(s) + 1: 
            return ""

        return s[final_start:final_start + min_len]


# class Solution:
#     def minWindow(self, s: str, t: str) -> str:

#         char_map = defaultdict(int)
#         for ch in t: 
#             char_map[ch] += 1

#         start, length, min_len = len(s), 0, len(s) + 1

#         for i in range(len(s)):
#             copy_map = char_map.copy()

#             j = i
#             length = 0
#             while j < len(s): 
#                 if not copy_map: 
#                     break
#                 if s[j] in copy_map: 
#                     if copy_map[s[j]] > 1: 
#                         copy_map[s[j]] -= 1
#                     else: 
#                         copy_map.pop(s[j])
#                 length += 1
#                 j += 1
            
#             if not copy_map: 
#                 if length < min_len: 
#                     start = i
#                     min_len = length

#         if start == len(s): 
#             return ""

#         return s[start:start + min_len]