class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == None:
            return 0
        window_size = len(needle)
        for i in range(len(haystack)):
            if (haystack[i:window_size+i] == needle):
                return i
        return -1