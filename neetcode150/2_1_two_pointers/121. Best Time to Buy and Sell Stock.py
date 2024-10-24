# 121. Best Time to Buy and Sell Stock - Easy
# url: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List


# time complexity: O(n), space complexity: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]  # keep track of the minimum price so far

        for price in prices:
            # find a new lower price, potentially a better buy
            if price < min_price:
                min_price = price

            max_profit = max(max_profit, price - min_price)
        return max_profit


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))  # 5
    print(s.maxProfit([7, 6, 4, 3, 1]))  # 0
