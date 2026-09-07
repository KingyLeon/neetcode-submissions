class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {} # val : index
        for i,n in enumerate(nums):
            difference = target - n
            # if(diff.get(difference) == None):
            if difference not in diff:
                diff[n] = i
            else:
                return [diff[difference], i]
        return 0