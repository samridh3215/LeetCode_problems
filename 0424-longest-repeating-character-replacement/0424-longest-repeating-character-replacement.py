class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        
        leftPointer = 0

        for rightPointer in range(len(s)):
            count[s[rightPointer]] = 1+count.get(s[rightPointer], 0)
            
            if(rightPointer-leftPointer+1 - max(count.values()))>k:
                count[s[leftPointer]] -=1
                leftPointer += 1
            
            res = max(res, rightPointer-leftPointer+1)
        
        return res