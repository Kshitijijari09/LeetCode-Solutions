# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find the mid 
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #reverse from middle
        prev,cur = None, slow
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            else:
                left = left.next
                right = right.next
        return True
            
        
        