class Solution:
    def maxProfit(self,prices:List[int]) -> int:
        sell1=sell2=0
        buy1=buy2=float('-inf')
        for i in prices:
            buy1=max(buy1,-i)
            sell1=max(sell1,i+buy1)
            buy2=max(buy2,sell1-i)
            sell2=max(sell2,i+buy2)
        return sell2
        