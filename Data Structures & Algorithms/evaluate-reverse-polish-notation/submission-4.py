import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        action_map = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a / b),
        }

        stack = []

        for token in tokens:
            if token not in action_map:
                stack.append(int(token))
            else:
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(action_map[token](n1, n2))

        return stack[-1]