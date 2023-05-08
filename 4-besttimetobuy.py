class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #bruteforce

        if len(prices) < 2: 
            return 0

        profit = 0

        for index, i in enumerate(prices): 
            for j in prices[index+1:]: 
                cur_profit = j - i
                if cur_profit > profit: 
                    profit = cur_profit
        return profit