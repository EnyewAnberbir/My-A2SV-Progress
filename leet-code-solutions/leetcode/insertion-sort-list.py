# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    prev = dummy  
    curr= head

    while curr:  
      next = curr.next  
      if prev.val >= curr.val:
        prev = dummy
      while prev.next and prev.next.val < curr.val:
        prev = prev.next
      curr.next = prev.next
      prev.next = curr
      curr = next 

    return dummy.next

