from list.ListNode import ListNode


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        用递归实现链表相邻互换：
        第一个节点的 next 是第三、第四个节点交换的结果，第二个节点的 next 是第一个节点；
        第三个节点的 next 是第五、第六个节点交换的结果，第四个节点的 next 是第三个节点；
        以此类推
        :param ListNode head
        :return ListNode
        """
        # 如果为 None 或 next 为 None，则直接返回
        if not head or not head.next:
            return head

        _next = head.next
        head.next = self.swapPairs(_next.next)
        _next.next = head
        return _next
