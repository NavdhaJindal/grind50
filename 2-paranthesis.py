class Solution:
    def isValid(self, s: str) -> bool:
        if ((s == '') or (s == '()') or (s == '{}') or (s == '[]')):
            return True
        elif (len(s) <= 2):
            return False
        else:
            index = 0
            while (index < len(s)):
                if (((s[index] == '(') and (s[index+1] == ')') )
                or ((s[index] == '{') and (s[index+1] == '}') )
                or ((s[index] == '[') and (s[index+1] == ']') )):
                    s = s[0:index] + s[index+2:]
                    index -= 1

                index +=1

        print(s)
        return self.isValid(s)