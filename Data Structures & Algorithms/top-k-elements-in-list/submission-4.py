class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = Counter(nums)
        numCount = [item for item, freq in numCount.most_common(k)]
        return numCount