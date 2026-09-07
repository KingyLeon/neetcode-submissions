class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        top = [item for item, freq in counts.most_common(k)]
        return top