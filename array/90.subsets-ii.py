from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int], sorted: bool = False) -> List[List[int]]:
        """回溯法，通过排序参数避免重复排序"""
        if not nums:
            return [[]]
        elif len(nums) == 1:
            return [[], nums]
        else:
            # 先排序，以便去重
            # 注意，这道题排序花的时间比较多
            # 因此，增加一个参数，使后续过程不用重复排序，可以大幅提高时间效率
            if not sorted:
                nums.sort()
            # 回溯法
            pre_lists = self.subsetsWithDup(nums[:-1], sorted=True)
            all_lists = [i + [nums[-1]] for i in pre_lists] + pre_lists
            # 去重
            result = []
            for i in all_lists:
                if i not in result:
                    result.append(i)
            return result


if __name__ == '__main__':
    print(Solution().subsetsWithDup([1,2,2]))
