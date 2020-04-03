import sys
from typing import List


class Solution:
    def s(self, nums: List[int]) -> List[int]:
        sums = [nums[0]]
        n = len(nums)
        for i in range(1, n):
            sums.append(sums[i - 1] + nums[i])
        return sums

    # 单词循环条件判断
    def tiaojiaopanduan(self, nums: List[int]) -> int:
        tmp = nums[0]
        max_ = tmp
        n = len(nums)
        for i in range(1, n):
            # 当当前序列加上此时的元素的值大于tmp的值，说明最大序列和可能出现在后续序列中，记录此时的最大值
            if tmp + nums[i] > nums[i]:
                max_ = max(max_, tmp + nums[i])
                tmp = tmp + nums[i]
            else:
                # 当tmp(当前和)小于下一个元素时，当前最长序列到此为止。以该元素为起点继续找最大子序列,
                # 并记录此时的最大值
                max_ = max(max_, tmp, tmp + nums[i], nums[i])
                tmp = nums[i]
        return max_

    # 解法三 - 优化前缀和 - from @lucifer
    # 我们定义函数 S(i) ，它的功能是计算以 0（包括 0）开始加到 i（包括 i）的值。
    #
    # 那么 S(j) - S(i - 1) 就等于 从 i 开始（包括 i）加到 j（包括 j）的值。
    #
    # 我们进一步分析，实际上我们只需要遍历一次计算出所有的 S(i), 其中 i = 0,1,2....,n-1。
    # 然后我们再减去之前的 S(k),其中 k = 0，1，i - 1，中的最小值即可。 因此我们需要 用一个变量来维护这个最小值，还需要一个变量维护最大值。
    #
    # 复杂度分析
    # 时间复杂度： O(n) - n 是数组长度
    # 空间复杂度： O(1)
    def qianzhuihe(self, nums: List[int]) -> int:
        n = len(nums)
        maxSum = nums[0]
        minSum = sum = 0
        for i in range(n):
            sum += nums[i]
            maxSum = max(maxSum, sum - minSum)
            minSum = min(minSum, sum)

        return maxSum

    # 我们把数组nums以中间位置（m)分为左（left)右(right)两部分.
    # 那么有， left = nums[0]...nums[m - 1] 和 right = nums[m + 1]...nums[n-1]
    #
    # 最大子序列和的位置有以下三种情况：
    #
    # 1.考虑中间元素nums[m], 跨越左右两部分，这里从中间元素开始，往左求出后缀最大，往右求出前缀最大, 保持连续性。
    # 2.不考虑中间元素，最大子序列和出现在左半部分，递归求解左边部分最大子序列和
    # 3.不考虑中间元素，最大子序列和出现在右半部分，递归求解右边部分最大子序列和
    # 分别求出三种情况下最大子序列和，三者中最大值即为最大子序列和。
    def fenzhi(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, nums, l, r):
        if l > r:
            return -sys.maxsize
        mid = (l + r) // 2
        left = self.helper(nums, l, mid - 1)
        right = self.helper(nums, mid + 1, r)
        left_suffix_max_sum = right_prefix_max_sum = 0
        sum = 0
        for i in reversed(range(l, mid)):
            sum += nums[i]
            left_suffix_max_sum = max(left_suffix_max_sum, sum)
        sum = 0
        for i in range(mid + 1, r + 1):
            sum += nums[i]
            right_prefix_max_sum = max(right_prefix_max_sum, sum)
        cross_max_sum = left_suffix_max_sum + right_prefix_max_sum + nums[mid]
        return max(cross_max_sum, left, right)

    # 动态规划
    def dynamic_programming(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum_ending_curr_index = max_sum = nums[0]
        for i in range(1, n):
            max_sum_ending_curr_index = max(max_sum_ending_curr_index + nums[i], nums[i])
            max_sum = max(max_sum_ending_curr_index, max_sum)

        return max_sum

if __name__ == '__main__':
    print(Solution().tiaojiaopanduan([15, -2, 1, -3, 4, -1, 2, 1, -5, 4, 9, -10]))
    print(Solution().fenzhi([15, -2, 1, -3, 4, -1, 2, 1, -5, 4, 9, -10]))
    print(Solution().dynamic_programming([-15, -2, 1, -3, 40, -1, 2, 1, -5, 4, 9, -10]))
    # print(5/2)
