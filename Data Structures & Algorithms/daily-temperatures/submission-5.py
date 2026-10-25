class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []
        
        q = deque()
        res = [0] * len(temperatures)
        for i,t in enumerate(temperatures):
            while q and temperatures[q[-1]] < t:
                index = q.pop()
                res[index] = i - index
            q.append(i)
        return res