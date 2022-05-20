class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ["(", "{", "["]:
                stack.append(i)
            else:
                if not stack:
                    return False
                j = stack.pop()
                if j == '(':
                    if i != ")":
                        return False
                if j == '{':
                    if i != "}":
                        return False
                if j == '[':
                    if i != "]":
                        return False
        if stack:
            return False
        return True
        
        