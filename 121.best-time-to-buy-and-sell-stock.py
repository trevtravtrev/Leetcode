#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if lower price found (before final array spot), max profit can only be higher so ignore previous
        max_profit = 0
        current_profit = 0
        lowest_price = prices[0]

        for price in prices[1:]:
            # lowest_price = min(lowest_price, price)
            if price < lowest_price:
                lowest_price = price
            else:
                current_profit = price - lowest_price
                # max_profit = max(max_profit, current_profit)
                if current_profit > max_profit:
                    max_profit = current_profit
        return max_profit

# @lc code=end

