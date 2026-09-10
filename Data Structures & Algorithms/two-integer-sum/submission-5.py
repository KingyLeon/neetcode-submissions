class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for i, n in enumerate(nums):
            sum = target - n
            if (sum not in numDict):
                numDict[n] = i
            else:
                return [numDict[sum], i]
        return [0, 0]