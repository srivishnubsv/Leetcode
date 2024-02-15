class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        pre = sum(nums)
        for num in sorted(nums, reverse=True):
            pre -= num
            if pre > num:
                return pre + num
        return -1
