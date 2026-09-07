class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i,n in enumerate(nums):
            difference = target - n
            if(diff.get(difference) == None):
                diff[n] = i
            else:
                return [diff[difference], i]
        return 0