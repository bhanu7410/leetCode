class Solution:
    def romanToInt(self, s: str) -> int:
        s=s[::-1]
        dit= {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            "C" : 100,
            'D' : 500,
            'M' : 1000
        }
        num=0
        for i in range(len(s)):
            if i==0: num+=dit[s[i]]
            elif s[i] == 'I':
                if s[i-1]=='X' or s[i-1]=='V': num-=1
                else: num+=1
            elif s[i] == 'X':
                if s[i-1]=='L' or s[i-1]=='C': num-=10
                else: num+=10
            elif s[i] == 'C':
                if s[i-1]=='D' or s[i-1]=='M': num-=100
                else: num+=100
            else:
                num+=dit[s[i]]
        return(num)