class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)-1):
            if(prices[i]<prices[i+1]):
                res += abs(prices[i]-prices[i+1])
        return res