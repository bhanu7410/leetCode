class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        x=''
        v=''
        a=0
        b=0
        for i in s:
            x+=i
            if i=='(':
                a+=1
            else:
                b+=1
            if a==b:
                v+=x[1:-1]
                x=''
        return v