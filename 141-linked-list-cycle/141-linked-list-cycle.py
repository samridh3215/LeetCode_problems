# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head
        s = set()
        if(temp== None):
            return False
        if (temp.next == None):
            return False
        temp  = head
        while (temp!=None):
            if (temp in s):
                return True
            s.add(temp)
            temp = temp.next
        return False
        
        
        