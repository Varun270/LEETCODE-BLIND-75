# Problem Link --> https://leetcode.com/problems/reverse-linked-list/

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        final_head = self.reverseList(head.next)
        
        head.next.next = head
        head.next = None
        return final_head