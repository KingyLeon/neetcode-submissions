class Solution:
    def isValid(self, s: str) -> bool:
        bracketStack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        for c in s:
            if c in closeToOpen:
                if bracketStack and bracketStack[-1] == closeToOpen[c]:
                    bracketStack.pop()
                else:
                    return False
            else:
                bracketStack.append(c)
        return True if not bracketStack else False