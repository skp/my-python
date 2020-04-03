from typing import List


class Solution:
    def _find_path(self, candidates, path, res, target, begin, size):
        if target == 0:
            res.append(path.copy())
        else:
            for i in range(begin, size):
                left_num = target - candidates[i]
                if left_num < 0:
                    break
                # 如果存在重复的元素，前一个元素已经遍历了后一个元素与之后元素组合的所有可能
                if i > begin and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                # 开始的 index 往后移了一格
                self._find_path(candidates, path, res, left_num, i + 1, size)
                path.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        与39题的区别是不能重用元素，而元素可能有重复；
        不能重用好解决，回溯的index往下一个就行；
        元素可能有重复，就让结果的去重麻烦一些；
        """
        size = len(candidates)
        if size == 0:
            return []

        # 还是先排序，主要是方便去重
        candidates.sort()

        path = []
        res = []
        self._find_path(candidates, path, res, target, 0, size)

        return res


if __name__ == '__main__':
    print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
