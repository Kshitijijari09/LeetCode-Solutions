# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        tmp = ListNode(0,head)
        prev,cur = tmp,head
        dup = -101
        
        while cur.next:
            if cur.val == cur.next.val:
                dup = cur.val
            
            if cur.val == dup:
                prev.next = cur.next
            else:
                print(prev.val,cur.val)
                prev = prev.next
            
            cur = cur.next
            
        if cur.val == dup:
            prev.next = None
        return tmp.next
            
            
            
            
        
        