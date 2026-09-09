class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn=float('inf')
        maxp=0
        for price in prices:
            if price<minn:
                minn=price
            elif price-minn>maxp:
                maxp=price-minn
        return maxp
            