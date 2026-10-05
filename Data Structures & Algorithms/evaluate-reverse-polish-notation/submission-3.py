# O(n) - time. O(n) - space.
import operator as op

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        floorDiv = lambda a, b: abs(a) // abs(b) * (1 if (a < 0) == (b < 0 ) else -1)
        operators = {"+": op.add, "-": op.sub, "*": op.mul, "/": floorDiv}

        for token in tokens:
            if token.lstrip("-").isnumeric():
                stack.append(int(token))
            else:
                elem1, elem2 = stack.pop(), stack.pop()
                operator = operators[token]
                stack.append(operator(elem2, elem1))


        return stack.pop()