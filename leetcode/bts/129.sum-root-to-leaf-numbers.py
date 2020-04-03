from leetcode.bts.TreeNode import TreeNode


class Solution:
    # 也可以用递归搞
    def sumNumbers(self, root: TreeNode) -> int:
        if not root: return 0
        result = 0
        node_queue, sum_queue = [root], [root.val]
        while node_queue:
            for i in node_queue:
                cur_node = node_queue.pop(0)
                cur_val = sum_queue.pop(0)
                if cur_node.left:
                    node_queue.append(cur_node.left)
                    sum_queue.append(cur_val * 10 + cur_node.left.val)
                if cur_node.right:
                    node_queue.append(cur_node.right)
                    sum_queue.append(cur_val * 10 + cur_node.right.val)
                if not (cur_node.left or cur_node.right):
                    result += cur_val
        return result