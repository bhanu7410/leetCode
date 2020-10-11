class Solution:
    def plusOne(self, digits) :
        n=0
        # digits= digits[::-1]
        for i in digits:
            n+=i
            n*=10
        n//=10
        n+=1
        return list(str(n))