# O(n) - time. O(n) - space.
class Solution:
    def isValid(self, s: str) -> bool:
        openingBrackets = set("[({")
        closingBrackets = set("})]")
        stack = list()

        for element in s:
            if element in openingBrackets:
                stack.append(element)
            else:
                match element:
                    case ")":
                        if len(stack) > 0 and stack[-1] == "(":
                            stack.pop()
                        else:
                            return False
                    case "]":
                        if len(stack) > 0 and stack[-1] == "[":
                            stack.pop()
                        else:
                            return False
                    case "}":
                        if len(stack) > 0 and stack[-1] == "{":
                            stack.pop()
                        else:
                            return False

        return len(stack) == 0