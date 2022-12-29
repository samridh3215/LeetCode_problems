class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            if ''.join(sorted(s)) not in res:
                res[''.join(sorted(s))]=[]
            res[''.join(sorted(s))].append(s)
                
            
        return list(res.values())