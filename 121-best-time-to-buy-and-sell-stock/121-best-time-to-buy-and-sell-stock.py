class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        profit = 0
        cursum = 0
        for i in range(len(prices)-1):
            cursum += (prices[i+1]- prices[i])
            if cursum<0:
                cursum = 0
            profit = max(profit, cursum)
        return profit