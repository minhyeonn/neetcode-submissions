# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        cur = dummy
        carryOver = 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            if v1 + v2 + carryOver >9:
                sum = v1 + v2 + carryOver - 10
                carryOver = 1
            else:
                sum = v1 + v2 + carryOver
                carryOver = 0
            cur.next = ListNode(sum, None)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carryOver == 1:
            cur.next = ListNode(1, None)
        return dummy.next
            