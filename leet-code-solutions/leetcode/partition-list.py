# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def partition(self, head: ListNode, x: int) -> ListNode:
    prev = ListNode(0)
    nexts = ListNode(0)
    left = prev
    right = nexts

    while head:
      if head.val < x:
        left.next = head
        left = head
      else:
        right.next = head
        right = head
      head = head.next

    right.next = None
    left.next = nexts.next

    return prev.next
            

            
             

