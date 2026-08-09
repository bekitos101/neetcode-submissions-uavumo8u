class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #prices = [10,1,5,6,7,1]
        #brute force solution: for the price bought on ith day, we record the profit 
        #if the stock is sold for all i+len(prices) and we record the max profit at each step   
        #this solutin is o(n2) time and o(1) space 
        #can we optimize further?
        # max_profit=0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         if prices[j]-prices[i]>max_profit:
        #             max_profit=prices[j]-prices[i]
        # return max_profit

        #optimized solution: Greedy approach 
        # At each ith day,we consider prices[i] as the potential sell price 
        # the greedy problem is trying to maximize profit= sell-buy 
        # maximize profit by minimizing buy (that's why we don't need to track the sell)
        # so at each ith day, if the current prices[i] < buy we update buy , otherwise we calculate the profit and we update the max_profit 

        max_profit=0
        min_buy=float("inf")
        for i in range(len(prices)):
            if prices[i]<min_buy:
                min_buy=prices[i]
            else:
                profit=prices[i]-min_buy
                max_profit=max(max_profit,profit)
        return int(max_profit)








        