class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        low = s.strip().split()
        return(len(low[-1]))
        