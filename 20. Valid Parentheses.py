class Solution(object):
    def isValid(self, s):
        stack = []
        match = {'(': ')', '[': ']', '{': '}'}
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            elif not stack or match[stack.pop()] != c:
                return False
        return not stack

s= [1,2,3,4,5]
print(s.pop())