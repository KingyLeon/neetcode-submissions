class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sizeOfSet = len(set(nums))
        return False if sizeOfSet == len(nums) else True