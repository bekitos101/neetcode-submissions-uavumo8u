class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #prices = [10,1,5,6,7,1]
        #brute force solution: for the price bought on ith day, we record the profit 
        #if the stock is sold for all i+len(prices) and we record the max profit at each step 
        max_profit=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j]-prices[i]>max_profit:
                    max_profit=prices[j]-prices[i]
        return max_profit






        