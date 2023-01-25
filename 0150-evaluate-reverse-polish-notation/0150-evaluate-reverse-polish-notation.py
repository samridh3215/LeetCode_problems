class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        for op in tokens:
            if op == '+':
                res.append(res.pop()+ res.pop())
            elif op == '-':
                n1, n2 = res.pop(), res.pop()
                res.append(n2-n1)
            elif op == '*':
                res.append(res.pop()*res.pop())
            elif op == '/':
                n1, n2 = res.pop(), res.pop()
                res.append(int(n2/n1))
            else:
                res.append(int(op))
        return res[0]
            