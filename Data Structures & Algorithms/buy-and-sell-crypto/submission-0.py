class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m,i,j=0,0,1
        while j<len(prices):
            if prices[i]>prices[j]:
                i=j
                j+=1
                continue
            d=prices[j]-prices[i]
            m=max(m,d)
            j+=1
        return m