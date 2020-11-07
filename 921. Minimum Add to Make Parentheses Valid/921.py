class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        xer=[]
        for i in S:
            if i == ")" and "("in xer :
                xer.pop()
            else :
                xer.append(i)
        return len(xer)