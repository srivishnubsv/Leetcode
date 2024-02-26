class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        str1=""
        for i in range(len(words)):
            str1+=words[i][0]
        if str1==s:
            return True
        else:
            return False
