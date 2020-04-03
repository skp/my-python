from typing import List

from bts.TreeNode import TreeNode


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if not n:
            return []

        def generateTree(start, end):
            if start > end:
                return [None]
            res = []
            for i in range(start, end + 1):
                ls = generateTree(start, i - 1)
                rs = generateTree(i + 1, end)
                for l in ls:
                    for r in rs:
                        node = TreeNode(i)
                        node.left = l
                        node.right = r
                        res.append(node)

            return res

        return generateTree(1, n)


if __name__ == '__main__':
        print(Solution().generateTrees(3))
