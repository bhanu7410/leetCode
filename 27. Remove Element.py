class Solution:
    def removeElement(self, nums, val: int) -> int:
        t=len(nums)
        i=0
        while i < t:
            if nums[i]==val:
                nums.pop(i)
                t-=1
                i-=1
            
            i+=1
        return len(nums)