class Solution:
    def removeDuplicates(self, nums):
        if len(nums) < 2:
                return len(nums)
        current = nums[0]
        old = 0
        count = 1
        i=1
        while i<len(nums):
            if nums[i]!= current :
                current = nums[i]
                nums[old + 1] = nums[i]
                old+=1
                count += 1
            i+=1
        return count