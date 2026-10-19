class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()
        bMap = {'(': ')', '{': '}', '[': ']'}
        for i, b in enumerate(s):
            if b in bMap:
                q.append(b)
            elif not q or bMap.get(q.pop()) != b:
                return False
        return len(q) == 0