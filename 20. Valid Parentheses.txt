class Solution:
    def isValid(self, s: str) -> bool:
        o=["[","(","{"]
        c=["]",")","}"]
        stk=[]
        for i in s:
            if i in o:
                stk.append(i)
            elif i in c:
                pos=c.index(i)
                if (len(stk)>0 and o[pos]==stk[len(stk)-1]):
                    stk.pop()
                else:
                    return False
        if (len(stk)==0):
            return True
        else:
            return False
