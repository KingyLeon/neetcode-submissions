class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = len(numbers) - 1
        while L < R:
            sum = numbers[L] + numbers[R]
            if (sum < target):
                L += 1
            elif (sum > target):
                R -= 1
            else:
                return [L+1, R+1]
        return [1,2]