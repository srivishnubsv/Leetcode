class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        N=m+n-2
        r=m-1
        f=1.0
        for i in range(1,r+1):
            f=f*(N-r+i)/i
        return int(f)
