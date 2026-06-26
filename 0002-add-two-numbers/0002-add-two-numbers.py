# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)        # dummy head for ease
        tail = dummy              # tail will build the result
        carry = 0

        p, q = l1, l2
        while p is not None or q is not None:
            x = p.val if p is not None else 0
            y = q.val if q is not None else 0

            s = x + y + carry
            carry = s // 10
            digit = s % 10

            tail.next = ListNode(digit)
            tail = tail.next

            if p is not None:
                p = p.next
            if q is not None:
                q = q.next

        # if there's remaining carry
        if carry:
            tail.next = ListNode(carry)

        return dummy.next
