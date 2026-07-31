# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return

        slow = head
        fast = head.next


        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        cur = slow.next
        slow.next = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        first = head
        second = prev
        while second:
            nxt = first.next
            prv = second.next
            first.next = second
            second.next = nxt
            first = nxt
            second = prv
        

            
            


        