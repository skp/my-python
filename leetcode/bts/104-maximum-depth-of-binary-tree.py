from leetcode.bts.TreeNode import TreeNode


class Solution:
    def maxDepth_rescursion(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        return 1 + max(self.maxDepth_rescursion(root.left), self.maxDepth_rescursion(root.right))

    # 前序遍历
    def maxDepth_queue(self, root: TreeNode) -> int:
        if not root:
            return 0
        # 用 None 分隔出一行
        q, depth = [root, None], 1
        while q:
            node = q.pop(0)
            if node:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            elif q:
                q.append(None)
                depth += 1
        return depth


if __name__ == '__main__':
    tree = TreeNode(3)
    tree.left = TreeNode(9)
    r = TreeNode(20)
    r.left = TreeNode(15)
    r.right = TreeNode(7)
    tree.right = r
    print(Solution().maxDepth_queue(tree))