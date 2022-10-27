# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l=0
        node=head
        while node:
            node,l=node.next,l+1
        node=head
        if l-n==0:
            return head.next
        count=0
        while node:
            count+=1
            if count==(l-n):
                print(node.val)
                node.next=node.next.next
            node=node.next
        return head