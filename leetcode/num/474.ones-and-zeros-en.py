from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        l = len(strs)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, l + 1):
            count0, count1 = strs[i - 1].count('0'), strs[i - 1].count('1')
            for i in reversed(range(count0, m + 1)):
                for j in reversed(range(count1, n + 1)):
                    dp[i][j] = max(dp[i][j], 1 + dp[i - count0][j - count1])
        return dp[m][n]


if __name__ == '__main__':
    Solution().findMaxForm(['10', '110'], 1, 1)
