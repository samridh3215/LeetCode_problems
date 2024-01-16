# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        temp1 = list1
        temp2 = list2
        if(temp1 ==None and temp2 == None ):
            return None
        while( temp1 != None and temp2 != None):
            if(temp1.val <= temp2.val):
                stack.append(temp1.val)
                temp1 = temp1.next
            else:
                stack.append(temp2.val)
                temp2 = temp2.next
        while(temp1 != None):
            stack.append(temp1.val)
            temp1  = temp1.next
        while(temp2 != None):
            stack.append(temp2.val)
            temp2 = temp2.next
        print(stack)
        head = ListNode(stack[0])
        temp = head
        for i in range(1, len(stack)):
            node = ListNode(stack[i])
            temp.next = node
            temp = temp.next
        return head