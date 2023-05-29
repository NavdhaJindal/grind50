class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charlocations = {}

        start = 0
        end = 0
        maxlen = 0
        currentlen = 0

        while end < len(s):
            if s[end] in charlocations: 
                start = max(charlocations[s[end]] + 1, start)

            charlocations[s[end]] = end
            end += 1
            currentlen = end - start
            maxlen = max(maxlen, currentlen)

        return maxlen