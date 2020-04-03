class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        :param list nums
        第二第三步 可以不用这么做 直接在第一步找下降点的每一步都 交换 如果找到下降点 停止 当前值就正好比之前大最小的粒度
        否则交换完毕也是最小的组合
        """
        # 第一步，从后往前，找到下降点
        down_index = None
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                down_index = i
                break
        # 如果没有下降点，重新排列
        if down_index is None:
            nums.reverse()
        # 如果有下降点
        else:
            # 第二步，从后往前，找到比下降点大的数，对换位置
            for i in range(len(nums) - 1, i, -1):
                if nums[down_index] < nums[i]:
                    nums[down_index], nums[i] = nums[i], nums[down_index]
                    break
            # 第三步，重新排列下降点之后的数
            i, j = down_index + 1, len(nums) - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
