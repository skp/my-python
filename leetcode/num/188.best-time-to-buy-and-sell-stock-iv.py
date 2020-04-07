from typing import List


# 买股票 最多能卖 k 次
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        if k < 1:
            return 0
        if k > len(prices) // 2:
            k = len(prices) // 2
        # 这是 完整的 状态转换过程 分别为 天、交易次数、是否持有
        # dp = [[[float('-inf') for _ in range(2)] for _ in range(k + 1)] for _ in range(len(prices))]
        # dp[0][0][0] = 0
        # dp[0][0][1] = -prices[0]
        # for i in range(1, len(prices)):
        #     for n in range(k, -1, -1):
        #         if n > (i + 1) // 2:
        #             continue
        #         dp[i][n][0] = max(dp[i - 1][n][0], dp[i - 1][n][1] + prices[i])
        #         dp[i][n][1] = max(dp[i - 1][n][1], dp[i - 1][n - 1][0] - prices[i])

        dp_ik0, dp_ik1 = [0 for _ in range(k + 1)], [0 for _ in range(k + 1)]
        dp_ik1[0] = float('-inf')
        dp_ik1[1] = -prices[0]
        for i in range(1, len(prices)):
            for n in range(k, 0, -1):
                if n > (i + 1) // 2:
                    continue
                dp_ik0[n] = max(dp_ik0[n], dp_ik1[n] + prices[i])
                dp_ik1[n] = max(dp_ik1[n], dp_ik0[n - 1] - prices[i])

        # 如果 k = 2 的情况
        # dp[i][2][0] = max(dp[i - 1][2][0], dp[i - 1][2][1] + prices[i])
        # dp[i][2][1] = max(dp[i - 1][2][1], dp[i - 1][1][0] - prices[i])
        # dp[i][1][0] = max(dp[i - 1][1][0], dp[i - 1][1][1] + prices[i])
        # dp[i][1][1] = max(dp[i - 1][1][1], -prices[i])
        #
        # dp_i10, dp_i11 = 0, float('-inf')
        # dp_i20, dp_i21 = 0, float('-inf')
        #
        # for price in prices:
        #     dp_i20 = max(dp_i20, dp_i21 + price)
        #     dp_i21 = max(dp_i21, dp_i10 - price)
        #     dp_i10 = max(dp_i10, dp_i11 + price)
        #     dp_i11 = max(dp_i11, -price)
        return dp_ik0[k]


if __name__ == '__main__':
    print(Solution().maxProfit(2, [7, 2, 9, 4, 7, 6]))
