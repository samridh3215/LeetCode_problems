class Solution:
    def longestCommonPrefix(self, strs):
        if strs == []:
            return ""
        short = min(strs, key=len)
        for i, ch in enumerate(short):
            for other in strs:
                if other[i] != ch:
                    return short[:i]
        return short

        