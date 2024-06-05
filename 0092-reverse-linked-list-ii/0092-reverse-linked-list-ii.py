# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right:return head
        times=right-left
        ans=prev=ListNode(None)
        prev.next=head
        cur=1
        while cur<left:
            cur+=1
            prev=prev.next
        fixed=prev.next
        cur=fixed.next
        for i in range(times):
            if not cur:break
            x=prev.next
            y=cur.next
            prev.next=cur
            cur.next=x
            fixed.next=y
            cur=y
        return ans.next