class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = 0
        y =x
        while x>0:
            s = s*10 + x%10
            x= x//10
        if (y == s):
            return True
        else: 
            return False
        
