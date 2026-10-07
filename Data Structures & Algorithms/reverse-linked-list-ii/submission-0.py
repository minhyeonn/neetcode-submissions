# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        before = dummy
        for _ in range(left - 1):          # node just before the range
            before = before.next

        start = before.next                # will become the range's tail
        prev, cur = None, start
        for _ in range(right - left + 1):  # standard reversal, exactly n nodes
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        # prev = new front of range, cur = first node after range (your 'border')
        before.next = prev
        start.next = cur
        return dummy.next
            

