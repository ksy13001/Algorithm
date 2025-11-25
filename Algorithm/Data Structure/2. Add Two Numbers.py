# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:  
        result = ListNode()
        current = result
        over = 0
        while l1 or l2 or over:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            temp = val1 + val2 + over
            if l1:
                l1 = l1.next    
            if l2:
                l2 = l2.next    
            over = temp//10
            temp %= 10
            current.next = ListNode(temp)
            current = current.next

        return result.next
