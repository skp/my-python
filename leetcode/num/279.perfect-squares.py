import sys


class Solution:
    def numSquares(self, k: int) -> int:
        if k <= 0:
            return 0
        dp = [sys.maxsize for _ in range(k + 1)]
        dp[0] = 0
        for i in range(1, k + 1):
            for j in range(1, k + 1):
                if pow(j, 2) > k:
                    break
                dp[i] = min(dp[i], dp[i - pow(j, 2)] + 1)
        return dp[k]


if __name__ == '__main__':
    print(Solution().numSquares(5))
