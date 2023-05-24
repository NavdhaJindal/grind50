class Solution:
    def climbStairs(self, n: int) -> int:
        def factorial (num):
            if num == 0 or num == 1:
                return 1
            return factorial(num - 1) * num

        totalNum = 0
        if n <= 0: 
            return 0

        for step2s in range(0, n//2 + 1):
            step1s = n - 2 * step2s
            totalNum += factorial(step1s + step2s) // (factorial(step1s) * factorial(step2s))

        return totalNum