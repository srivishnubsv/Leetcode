class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l1=[]
        c=0
        for i in nums:
            l1.append(c+i)
        return l1
