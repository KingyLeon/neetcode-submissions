class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()
        for i, b in enumerate(s):
            bMap = {'(': ')', '{': '}', '[': ']'}
            # Check if bracket is opener or closer
            if b not in bMap.keys():
                # check if the queue is empty, if its empty and is closer then false
                if (len(q) > 0):
                    if bMap.get(q.pop()) != b:
                        return False
                else:
                    return False
            else:
                q.append(b)
        return len(q) == 0