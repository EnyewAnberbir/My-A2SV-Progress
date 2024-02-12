# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        stack = []
        check = True
        while slow:
            stack.append(slow.val)
            slow = slow.next
        while head:
            i = stack.pop()
            if head.val != i:
                check = False
                break
            head = head.next
        return check
        