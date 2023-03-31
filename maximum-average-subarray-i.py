# https://leetcode.com/problems/maximum-average-subarray-i/



class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        win_sum = sum(nums[:k])
        max_average = win_sum/float(k)

        for i in range(len(nums) - k):
            win_sum += nums[i + k] - nums[i]
            max_average = max(max_average, win_sum/ float(k))

        return max_average
