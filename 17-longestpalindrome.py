class Solution:
    def longestPalindrome(self, s: str) -> int:
        ch_dict = {}
        for ch in s:
            ch_dict[ch] = ch_dict.get(ch, 0) + 1
        
        singular = 0
        palindrome_length = 0
        for ch in ch_dict:
            if (ch_dict[ch] % 2 != 0 and singular == 0):
                singular = ch_dict[ch]
            elif (ch_dict[ch] >= 2):
                palindrome_length += (ch_dict[ch] // 2) * 2
        
        return palindrome_length + singular