class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         profit = max(prices[j]-prices[i], profit)
        # return profit
        
        profit = 0
        mini = prices[0]
        for i in range(1, len(prices)):
            profit = max(profit, prices[i]-mini)
            mini = min(prices[i], mini)
        return profit