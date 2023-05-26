# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        numNodes = 0

        temp = head

        while temp: 
            numNodes += 1
            temp = temp.next

        for i in range(numNodes//2):
            head = head.next

        return head