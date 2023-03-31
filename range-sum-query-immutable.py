# https://leetcode.com/problems/range-sum-query-immutable/



class NumArray:

    def __init__(self, nums: List[int]):
        self.pre = [0]
        total = 0
        for num in nums:
            total += num
            self.pre.append(total)

    def sumRange(self, left: int, right: int) -> int:
        return self.pre[right + 1] - self.pre[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
