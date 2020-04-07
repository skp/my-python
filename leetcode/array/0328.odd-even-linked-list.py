from leetcode.list.ListNode import ListNode


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        h = head
        odd = head
        p = head.next
        even = head.next
        while odd and even and even.next:
            odd.next = even.next
            even.next = odd.next.next

            odd = odd.next
            even = even.next
        odd.next = p
        return h


if __name__ == '__main__':
    head = ListNode(1)
    h2 = ListNode(2)
    head.next = h2
    h3 = ListNode(3)
    h2.next = h3
    h4 = ListNode(4)
    h3.next = h4
    h5 = ListNode(5)
    h4.next = h5
    # h6 = ListNode(6)
    # h5.next = h6
    print(Solution().oddEvenList(head))