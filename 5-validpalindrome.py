class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r: 
            if not s[l].isalnum():
                l+=1
            elif not s[r].isalnum():
                r-=1
            else: 
                if s[l].lower() != s[r].lower():
                    return False
                l+=1
                r-=1
        return True
        # s = s.lower()
        # print(s)
        # str1 = ''.join(filter(str.isalnum, s))
        # print(str1)
        # str2 = ''.join(str1[i] for i in range(len(str1)-1, -1, -1))
        # print(str2)
        # if str1 == str2: 
        #     return True
        # else: 
        #     return False