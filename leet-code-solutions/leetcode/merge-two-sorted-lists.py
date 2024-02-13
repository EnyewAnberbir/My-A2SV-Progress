# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = list1
        node2 = list2
        curr = ListNode(-102)
        prev = curr

        while node1 or node2:
            if node1 is None:
                
                prev.next = node2
                prev = prev.next
                node2 = node2.next
            elif node2 is None:
                
                prev.next = node1
                prev = prev.next
                node1 = node1.next
            elif node1 and node2:
                if node1.val > node2.val:
                    
                    prev.next = node2
                    prev = prev.next
                    node2 = node2.next
                else:
                    
                    prev.next = node1
                    prev = prev.next
                    node1 = node1.next
            else:
                break
        return curr.next




