class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        maps={"I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000}
        result =0
        for i in range(len(s)-1):
            if(maps[s[i]]<maps[s[i+1]]):
                result -= maps[s[i]] 
            else:
                result+= maps[s[i]] #this goes till the second last #lement
        return (result+maps[s[-1]]) # we add maps[s[-1]] to get the last #umber 
        