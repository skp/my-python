from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for j in coins:
                if j > i:
                    continue
                dp[i] = min(dp[i], dp[i - j] + 1)
        return -1 if dp[-1] == amount + 1 else dp[-1]


if __name__ == '__main__':
    print(Solution().coinChange([1,2,5], 100))