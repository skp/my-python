class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        ret = s[0]
        l = len(s)
        dp = [[0 for _ in range(l)] for _ in range(l)]
        # i 开始位置 j 结束位置
        for i in range(l - 1, -1, -1):
            for j in range(i, l):
                if i == j:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[0][l - 1]


if __name__ == '__main__':
    print(Solution().longestPalindromeSubseq("bbbab"))
    print(Solution().longestPalindromeSubseq("bbbabb"))
