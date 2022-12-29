# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        returnHead = head
        stack = []
        while(returnHead.next!= None):
            stack.append(returnHead.val)
            returnHead = returnHead.next
        temp = returnHead
        while(head!=returnHead and temp!=None):
            temp.next = ListNode(stack.pop())
            head = head.next
            temp = temp.next
        return returnHead
        