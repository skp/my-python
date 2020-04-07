from typing import List

# 买股票 卖完了有一天一冷冻期
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        dp_i_0, dp_i_1, dp_prev_0 = 0, -prices[0], 0
        for i in range(1, len(prices)):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_prev_0 - prices[i])
            dp_prev_0 = temp
        return dp_i_0


if __name__ == '__main__':
    print(Solution().maxProfit([7, 2, 9, 4, 7, 6]))
