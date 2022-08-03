class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r= {}
        m = {}
        for i in magazine:
            if i in m:
                m[i]+=1
            else:
                m[i] = 1
                
        for i in ransomNote:
            if i not in magazine:
                return False
            if ransomNote.count(i) > m[i]:
                return False
        return True