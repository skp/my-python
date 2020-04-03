from typing import Dict

from bts.TreeNode import TreeNode


class Solution:
    # 递归
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        cur = self.helper(root, sum)
        l = self.pathSum(root.left, sum)
        r = self.pathSum(root.right, sum)
        return cur + l + r

    def helper(self, cur, sum) -> int:
        if not cur:
            return 0
        lPathNum = self.helper(cur.left, sum - cur.val)
        rPathNum = self.helper(cur.right, sum - cur.val)
        return lPathNum + rPathNum + (1 if cur.val == sum else 0)

    # 用 map 保存记录
    # accumulate
    # vt.积攒
    # vi.累积；积聚
    def pathSum1(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        return self.helper1(root, 0, sum, {})

    def helper1(self, root: TreeNode, acc, sum: int, map: Dict) -> int:
        if not root:
            return 0
        count = 0
        acc += root.val
        if acc == sum:
            count += 1
        if root.val == sum:
            count += 1
        if map[acc - sum] != 0:
            count += map[acc - sum]
        if map[acc] == 0:
            map[acc] = 0
        else:
            map[acc] += 1
        ret = count + self.helper1(root.left, acc, sum, map) + self.helper1(root.right, acc, sum, map)
        # 这个操作 花一个 二叉树的图就明白了， 在操作下一个节点的时候 要排除前一个节点的值 因为 这个节点 不在自己这条分支上
        map[acc] -= 1
        return ret