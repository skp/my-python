from typing import List
from leetcode.bts.TreeNode import TreeNode


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return

        stack, ret = [root], []
        p = root
        while stack:
            top = stack[-1]
            if top.left == p or top.right == p or (not top.left and not top.right):
                p = stack.pop()
                ret.append(p.val)
            else:
                if top.right:
                    stack.append(top.right)
                if top.left:
                    stack.append(top.left)
        return ret

    # 后序遍历是 左-右-根 的顺序， 这里取巧反向根-右-左输入，再反向输出
    def postorderTraversal1(self, root: TreeNode) -> List[int]:
        r, stack = [], root and [root] or []
        while stack:
            root = stack.pop()
            r.append(root.val)
            stack += root.left and [root.left] or []
            stack += root.right and [root.right] or []
        return r[::-1]

    def postorderTraversal2(self, root: TreeNode) -> List[int]:
        return root and sum((*map(self.postorderTraversal2, [root.left, root.right]), [root.val]), []) or []



if __name__ == '__main__':
    tree = TreeNode(3)
    tree.left = TreeNode(9)
    r = TreeNode(20)
    r.left = TreeNode(15)
    r.right = TreeNode(7)
    tree.right = r
    print(Solution().postorderTraversal(tree))
    print(Solution().postorderTraversal1(tree))
    print(Solution().postorderTraversal2(tree))