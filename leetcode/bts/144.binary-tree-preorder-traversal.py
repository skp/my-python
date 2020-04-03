from typing import List
from leetcode.bts.TreeNode import TreeNode


# 前序
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node is None:
                continue
            else:
                result.append(node.val)
                # 左右节点还需继续深化，并且入栈是先右后左
                stack.append(node.right)
                # 节点自身已遍历，回头可以直接取值
                stack.append(node.left)
        return result


if __name__ == '__main__':
    tree = TreeNode(3)
    tree.left = TreeNode(9)
    r = TreeNode(20)
    r.left = TreeNode(15)
    r.right = TreeNode(7)
    tree.right = r
    print(Solution().preorderTraversal(tree))
