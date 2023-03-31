# https://leetcode.com/problems/running-sum-of-1d-array/



class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0
        result = []
        
        for i, num in enumerate(nums):
            total += num
            result.append(total)
        return result
