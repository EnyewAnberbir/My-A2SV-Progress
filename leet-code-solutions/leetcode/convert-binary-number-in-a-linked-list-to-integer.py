# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        curr = head
        coll = []
        summ = 0
        while curr:
            coll.append(curr.val)
            curr = curr.next
        n = len(coll)
        for i in range(n):
            n-=1
            summ+=coll[i] * 2**n
        return summ

        
            
    