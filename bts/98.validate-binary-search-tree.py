from typing import List
from bts.TreeNode import TreeNode


# 中序 在二叉搜索树中是 升序
# 一个二叉搜索树是否正确 看中序是否正确
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 递归法
        # if root is None:
        #     return []
        # return self.inorderTraversal(root.left)\
        #     + [root.val]\
        #     + self.inorderTraversal(root.right)
        # 迭代法
        stack = []
        prev = float('-inf')
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val < prev:
                return False
            prev = root.val
            root = root.right
        return True

    # 定义法
    def isValidBST2(self, root: TreeNode, area: tuple = (-float('inf'), float('inf'))) -> bool:
        """思路如上面的分析，用Python表达会非常直白
        :param root TreeNode 节点
        :param area tuple 取值区间
        """
        if root is None:
            return True

        is_valid_left = root.left is None or (root.left.val < root.val and area[0] < root.left.val < area[1])
        is_valid_right = root.right is None or (root.right.val > root.val and area[0] < root.right.val < area[1])

        # 左右节点都符合，说明本节点符合要求
        is_valid = is_valid_left and is_valid_right

        # 递归下去
        return is_valid and self.isValidBST(root.left, (area[0], root.val)) and self.isValidBST(root.right, (root.val, area[1]))
