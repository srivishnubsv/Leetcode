class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans=[]
        pos=[]
        neg=[]
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)
        for p,n in zip(pos,neg):
            ans+=[p,n]
        return ans
