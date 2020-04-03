from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums:
            slow = 0
            for fast in range(1, len(nums)):
                if nums[fast] != nums[slow]:
                    slow += 1
                    nums[slow] = nums[fast]
            print(nums)
            return slow + 1
        else:
            return 0


if __name__ == '__main__':
    print(Solution().removeDuplicates([0, 0, 1, 2, 3, 3, 3, 4, 7, 8, 9]))
