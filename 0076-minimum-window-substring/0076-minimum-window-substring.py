class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""

        tDic = {}
        for i in t:
            tDic[i] = 1 + tDic.get(i, 0)
        winDic = {}
        have, need = 0, len(tDic)
        l = 0
        ans = [-1, -1]
        res = float("infinity")
        for r in range(len(s)):
            c = s[r]
            winDic[c] = 1 + winDic.get(c, 0)   
            if c in tDic and tDic[c] == winDic[c]:
                have+=1
            while have == need:
                if(r-l+1) < res:
                    ans = [l, r]
                    res = r-l+1
                winDic[s[l]] -= 1
                if s[l] in tDic and winDic[s[l]] < tDic[s[l]]:
                    have-=1
                l+=1
        l, r = ans
        if(res != float("infinity")):
            return s[l:r+1]
        else:
            return ""

