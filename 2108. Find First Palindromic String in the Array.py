class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        s=""
        for i in words:
            if i==i[::-1]:
                s=s+i
                break
        if len(s)==0:
            return str()
        else:
            return s
