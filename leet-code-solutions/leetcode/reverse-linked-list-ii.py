# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
    if not head and m == n:
      return head

    dummy = ListNode(0, head)
    prev = dummy

    for _ in range(m - 1):
      prev = prev.next 

    tail = prev.next 
    for _ in range(n - m):
      last = tail.next
      tail.next = last.next
      last.next = prev.next
      prev.next = last

    return dummy.next