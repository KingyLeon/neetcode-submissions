class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()
        mp = {'(': ')', '[': ']', '{': '}'}
        if len(s) == 1 or not s:
            return False
        for c in s:
            if c in mp:
                q.append(c)
            else:
                if not q or mp[q[-1]] != c:
                    return False
                else:
                    q.pop()
        return not q