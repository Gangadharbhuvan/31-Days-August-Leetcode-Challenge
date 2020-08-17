'''
	Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # edge case of nothing to buy and sell
        if len(prices) < 2:
            return 0
        # edge case of only two days
        if len(prices) == 2:
            return max(0, prices[1] - prices[0])
        
        one = -sys.maxsize-1
        two = 0
        three = -sys.maxsize-1
        four = 0
        i = 0
        while i < len(prices):
            one = max(one, -prices[i])
            two = two if i>=len(prices)-1 else max(two, one + prices[i+1])
            three = three if i>=len(prices)-2 else max(three, two - prices[i+2])
            four = four if i>=len(prices)-3 else max(four, three + prices[i+3])
            i+=1
        
        return max(two, four)