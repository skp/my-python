from list.ListNode import ListNode


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        tmpFirst = ListNode(0)
        tmpFirst.next = head
        cur = tmpFirst
        while cur.next:
            if cur.next != val:
                cur = cur.next
            else:
                cur.next = cur.next.next
        return tmpFirst.next283.move-zeroes
