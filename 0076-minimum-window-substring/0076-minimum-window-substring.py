class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""

        tDic = {}  #Create a count record of all characters 
        for i in t:
            tDic[i] = 1 + tDic.get(i, 0)
        winDic = {} #store charcter and count of sliding window
        have, need = 0, len(tDic)  # have and need should match i.e a substring is present in s
        l = 0 #left pointer 
        ans = [-1, -1]  #to store the ends of left and right pointers
        res = float("infinity")
        for r in range(len(s)):
            c = s[r]
            winDic[c] = 1 + winDic.get(c, 0)     #update window dicttionary
            if c in tDic and tDic[c] == winDic[c]:  # updating have value if it exists in t
                have+=1 
            while have == need:  # to check and update if its minimum length window 
                if(r-l+1) < res:
                    ans = [l, r]
                    res = r-l+1
                winDic[s[l]] -= 1 # remove the the left character in wndow 
                if s[l] in tDic and winDic[s[l]] < tDic[s[l]]:  # update have value 
                    have-=1
                l+=1  # move the left pointer
        l, r = ans  # deconstruct the array to get left and right pointers of window
        if(res != float("infinity")):
            return s[l:r+1] 
        else:
            return ""

