class Solution:
    def addBinary(self, a: str, b: str) -> str:

        # stack = []
        # carry = '0'
        # for i in range(-1:-max(len(a), len(b)):-1):
        #     if -i > len(a)
        
        carry = 0
        result = ''

        a = list(a)
        b = list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            result += str(carry %2)
            carry //= 2

        return result[::-1]