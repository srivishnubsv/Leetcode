class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x=[]
        res=[]
        for i in range(len(points)):
            x.append(points[i][0])
        x.sort()
        for i,j in zip(x[1:],x):
            res.append(i-j)
        return max(res) 
