from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        sum = 0
        for i in nums:
            sum += i
        if sum & 1 == 1:
            return False
        target = sum >> 1

        dp = [[False for _ in range(target + 1)] for _ in range(len(nums) + 1)]
        for i in range(1, len(nums) + 1):

            dp[i - 1][0] = True
            for j in range(0, target + 1):
                if j < nums[i - 1]:
                    continue
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
        return dp[len(nums)][target]


if __name__ == '__main__':
    print(Solution().canPartition([1, 5, 11, 5, 92,77,19123123]))
