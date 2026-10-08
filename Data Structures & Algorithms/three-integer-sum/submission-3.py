class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        for i,n in enumerate(nums):
            L = i+1
            R = len(nums) - 1
            if i > 0 and n == nums[i-1]:
                continue
            while L < R:
                sum = n + nums[L] + nums[R]
                if (sum < 0):
                    L += 1
                elif (sum > 0):
                    R -= 1
                else:
                    results.append([nums[L], nums[R], n])
                    L += 1
                    R -= 1
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
                    while L < R and nums[R] == nums[R + 1]:
                        R -= 1
        return results