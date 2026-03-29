class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #brute force 
        #prices = [10,1,5,6,7,1]
        # traverse the prices array 
        # for each day check if the selling price makes profit 
        # update the max_profit accordingly 
        # time complexity O(n2) space complexity O(1)
        
        # max_profit=0
        # for i,price in enumerate(prices):
        #     for j in range(i+1,len(prices)):
        #         profit= prices[j]-price
        #         if profit<0:
        #             profit=0 
        #         max_profit=max(max_profit,profit)
        # return max_profit 

        #optimized solution 
        #minimum buying price for the maximum selling price 
        #prices=[10,1,5,6,7,1]
        #min_buy=1 max_sell=7
        
        min_buy=float('inf')
        max_profit=0
        for i, price in enumerate(prices):
            if price<min_buy:
                #if the buying price is less than the one we have we update the buying price 
                min_buy=min(min_buy,price)
            else:
                #otherwise we pretend like we sell today 
                profit=price-min_buy 
                if profit<0:
                    profit=0
                max_profit=max(profit,max_profit)
        return max_profit

                


        


        