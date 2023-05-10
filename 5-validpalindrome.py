class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        print(s)
        str1 = ''.join(filter(str.isalnum, s))
        print(str1)
        str2 = ''.join(str1[i] for i in range(len(str1)-1, -1, -1))
        print(str2)
        if str1 == str2: 
            return True
        else: 
            return False