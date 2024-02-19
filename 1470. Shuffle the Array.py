class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n1=[]
        n2=[]
        ans=[]
        for i in range(len(nums)):
            if i<n:
                n1.append(nums[i])
            else:
                n2.append(nums[i])
        for i,j in zip(n1,n2):
            ans.append(i)
            ans.append(j)
        return ans
