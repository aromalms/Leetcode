class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pointer=1
        profit=0
        while pointer<len(prices):
            #profitable
            if prices[pointer]>prices[pointer-1]:
                profit=profit+(prices[pointer]-prices[pointer-1])
            pointer+=1
        return profit
