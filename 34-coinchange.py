class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # recursive solution
        # at each recursive step, we add one of the denominations to the sum until it adds up to the total
        # return the fewest numbers
        #base case: when the total has been exceeded, or when it's equal to the total
        #equal: 
        coins.sort()
        def recur_sum(amount, i) -> int:
            if amount == 0:
                return 0
            if i < 0: 
                return sys.maxsize
            if amount < 0: 
                return sys.maxsize
            else: 
                ans = 1 + min(recur_sum(amount - coins[i], i-1), recur_sum(amount - coins[i], i))
                print(amount)
                print(ans)
                return ans
        
        result = recur_sum(amount, len(coins) - 1)
        if result >= sys.maxsize: 
            return -1
        if result == 0:
            return 0
        else:
            return result - 1