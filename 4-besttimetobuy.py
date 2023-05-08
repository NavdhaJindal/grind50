class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #faulty 
        
        begin = 0
        end = len(prices)-1

        profit = prices[end] - prices[begin]

        while begin < end:
            if (prices[end - 1] - prices[begin] > profit):
                profit = prices[end - 1] - prices[begin]
                end = end - 1
            elif (prices[end] - prices[begin + 1] > profit):
                profit = prices[end] - prices[begin + 1]
                begin = begin + 1
            else:
                end = end - 1
                begin = begin + 1
        
        if (profit > 0):
            return profit
        else: 
            return 0
    

        #bruteforce

        # if len(prices) < 2: 
        #     return 0

        # profit = 0

        # for index, i in enumerate(prices): 
        #     for j in prices[index+1:]: 
        #         cur_profit = j - i
        #         if cur_profit > profit: 
        #             profit = cur_profit
        # return profit