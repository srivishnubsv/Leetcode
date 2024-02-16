import collections
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cnt = Counter(arr)
        for i, j in enumerate(sorted(cnt.values())):
            k -= j
            if k < 0:
                return len(cnt) - i
        return 0
