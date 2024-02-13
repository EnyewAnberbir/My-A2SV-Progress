# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
  def deleteDuplicates(self, head: ListNode) -> ListNode:
    prev = ListNode(-102)
    curr = head

    while curr :
        if prev.val == curr.val:
            while curr and curr.val == prev.val:  
                curr = curr.next
                
            prev.next = curr
        
        prev = curr
        if curr:
            curr = curr.next

    return head


    


    
