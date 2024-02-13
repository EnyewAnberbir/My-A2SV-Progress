# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        if not head or not head.next:
            return head
        curr2 = head.next
        curr3 = curr2
        while curr and curr2 and curr2.next :
            curr.next= curr2.next
            curr = curr.next

            curr2.next = curr.next
            curr2 = curr2.next

        curr.next = curr3


        return head


    
        
        
        