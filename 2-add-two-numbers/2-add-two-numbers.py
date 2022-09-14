# Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        s1 = ""
        s2 = ""
        def num(l, s):
            if(l==None):
                return int(s[::-1])
            s = s+(str(l.val))
            return num(l.next, s)
        n = num(l1,s1)+num(l2,s2)
        n_str = str(n)[::-1]
        head = ListNode(int(n_str[0]))
        temp = head
        for i in range(1, len(n_str)):
            temp.next = ListNode(int(n_str[i]))
            temp = temp.next
        return head
        