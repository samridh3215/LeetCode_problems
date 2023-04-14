class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size = len(s1)
        d1 = {s1[i]: s1.count(s1[i]) for i in range(size)}
        for i in range(len(s2)-size+1):
            d2 = {}
            for j in range(i, i+size):
                if s2[j] in d2.keys():
                    d2[s2[j]]+=1
                else:
                    d2[s2[j]] = 1
            # d2 = {c: subStr.count(c) for c in subStr}
            print(d1, d2)
            if d1 == d2:
                return True
        return False