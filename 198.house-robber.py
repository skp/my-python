from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        else:
            pre, cur = nums[0], nums[1]
            for i in range(2, len(nums)):
                pre, cur = cur, max(pre + nums[i], cur)
            return cur


if __name__ == '__main__':
    print(Solution().rob([1, 2, 3, 1]))
    print(Solution().rob([2,7,9,3,1,10]))
