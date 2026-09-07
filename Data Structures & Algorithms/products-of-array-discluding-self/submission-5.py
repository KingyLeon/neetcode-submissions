class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        Total = math.prod(nums)
        for i in range(len(nums)):
            if (nums[i] == 0):
                leftSide = math.prod(nums[0: i])
                rightSide = math.prod(nums[i+1: len(nums)])
                output.append(leftSide * rightSide)
            else:
                divisedTotal = int(Total / nums[i])
                output.append(divisedTotal)
        return output
