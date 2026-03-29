class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #brute force 
        #prices = [10,1,5,6,7,1]
        # traverse the prices array 
        # for each day check if the selling price makes profit 
        # update the max_profit accordingly 

        max_profit=0
        for i,price in enumerate(prices):
            for j in range(i+1,len(prices)):
                profit= prices[j]-price
                if profit<0:
                    profit=0 
                max_profit=max(max_profit,profit)
        return max_profit 
