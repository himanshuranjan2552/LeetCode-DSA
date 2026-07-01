# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        ll = ListNode(0)
        ptr = ll
        carry = 0 

        while l1 is not None or l2 is not None or carry>0 :

            if l1 is not None:
                n1 = l1.val
            else:
                n1 = 0

            if l2 is not None:
                n2 = l2.val
            else:
                n2 = 0

            total = n1 + n2 + carry

            carry = total // 10

            ptr.next = ListNode(total % 10)
            ptr = ptr.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return ll.next


