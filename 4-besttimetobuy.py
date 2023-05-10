class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        maxprofit = 0

        while (sell < len(prices)): 
            cur_profit = prices[sell] - prices[buy]
            if cur_profit < 0:
                buy = sell
                sell = buy + 1
            else:
                if cur_profit > maxprofit: 
                    maxprofit = cur_profit
                sell = sell + 1
        
        return maxprofit
            

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

        # begin = 0
        # end = len(prices)-1

        # profit = prices[end] - prices[begin]

        # while begin < end:
        #     if (prices[end - 1] - prices[begin] > profit):
        #         profit = prices[end - 1] - prices[begin]
        #         end = end - 1
        #     elif (prices[end] - prices[begin + 1] > profit):
        #         profit = prices[end] - prices[begin + 1]
        #         begin = begin + 1
        #     else:
        #         end = end - 1
        #         begin = begin + 1
        
        # if (profit > 0):
        #     return profit
        # else: 
        #     return 0

        #faulty 

        # begin = 0
        # end = len(prices)-1

        # profit = prices[end] - prices[begin]

        # while begin < end:
        #     if (prices[end - 1] - prices[begin] > profit):
        #         profit = prices[end - 1] - prices[begin]
        #         end = end - 1
        #     elif (prices[end] - prices[begin + 1] > profit):
        #         profit = prices[end] - prices[begin + 1]
        #         begin = begin + 1
        #     else:
        #         end = end - 1
        #         begin = begin + 1
        
        # if (profit > 0):
        #     return profit
        # else: 
        #     return 0
    

        #bruteforce
        #too long
        # if len(prices) < 2: 
        #     return 0

        # profit = 0

        # for index, i in enumerate(prices): 
        #     for j in prices[index+1:]: 
        #         cur_profit = j - i
        #         if cur_profit > profit: 
        #             profit = cur_profit
        # return profit