class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count=0
        t = len(nums)
        l=[]
        for i in range(t-1):
            if nums[i] in set(l):
                continue
            if nums.count(nums[i])> 1 :
                n= nums.count(nums[i])
                count+=n*(n-1)//2
                l.append(nums[i])
        return count